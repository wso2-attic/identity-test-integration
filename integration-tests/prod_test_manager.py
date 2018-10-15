# Copyright (c) 2018, WSO2 Inc. (http://wso2.com) All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# importing required modules
import sys
from xml.etree import ElementTree as ET
import subprocess
import wget
import logging
import inspect
import os
import shutil
import pymysql
import sqlparse
import re
from pathlib import Path
import urllib.request as urllib2
from xml.dom import minidom
import intg_test_manager as cm
from subprocess import Popen, PIPE

from prod_test_constant import DB_META_DATA, DIST_POM_PATH, INTEGRATION_PATH, DISTRIBUTION_PATH, \
    DATASOURCE_PATHS, LIB_PATH, WSO2SERVER, M2_PATH, ARTIFACT_REPORTS_PATHS

from intg_test_constant import NS, ZIP_FILE_EXTENSION, CARBON_NAME, VALUE_TAG, SURFACE_PLUGIN_ARTIFACT_ID, TEST_PLAN_PROPERTY_FILE_NAME, \
    INFRA_PROPERTY_FILE_NAME, LOG_FILE_NAME, PRODUCT_STORAGE_DIR_NAME, DEFAULT_DB_USERNAME, LOG_STORAGE, TEST_OUTPUT_DIR_NAME, \
    DEFAULT_ORACLE_SID, MYSQL_DB_ENGINE, ORACLE_DB_ENGINE, PRODUCT_STORAGE_DIR_NAME, MSSQL_DB_ENGINE

database_names = []
storage_dir_abs_path = None
use_custom_testng_file=None
db_engine = None
sql_driver_location = None

def get_db_meta_data(argument):
    switcher = DB_META_DATA
    return switcher.get(argument, False)


#TODO: Improve the method in generic way to support all products
def add_distribution_to_m2(storage, name, product_version):
    """Add the distribution zip into local .m2.
    """
    home = Path.home()
    m2_rel_path = ".m2/repository/org/wso2/" + M2_PATH[cm.product_id]
    linux_m2_path = home / m2_rel_path / product_version / name
    windows_m2_path = Path("/Documents and Settings/Administrator/" + m2_rel_path + "/" + product_version + "/" + name)
    if sys.platform.startswith('win'):
        windows_m2_path = cm.winapi_path(windows_m2_path)
        storage = cm.winapi_path(storage)
        cm.compress_distribution(windows_m2_path, storage)
        shutil.rmtree(windows_m2_path, onerror=cm.on_rm_error)
    else:
        cm.compress_distribution(linux_m2_path, storage)
        shutil.rmtree(linux_m2_path, onerror=cm.on_rm_error)


def modify_datasources():
    for data_source in datasource_paths:
        file_path = Path(storage_dist_abs_path / data_source)
        if sys.platform.startswith('win'):
            file_path = cm.winapi_path(file_path)
        logger.info("Modifying datasource: " + str(file_path))
        artifact_tree = ET.parse(file_path)
        artifarc_root = artifact_tree.getroot()
        data_sources = artifarc_root.find('datasources')
        for item in data_sources.findall('datasource'):
            database_name = None
            for child in item:
                if child.tag == 'name':
                    database_name = child.text
                # special checking for namespace object content:media
                if child.tag == 'definition' and database_name:
                    configuration = child.find('configuration')
                    url = configuration.find('url')
                    user = configuration.find('username')
                    password = configuration.find('password')
                    validation_query = configuration.find('validationQuery')
                    drive_class_name = configuration.find('driverClassName')
                    if MYSQL_DB_ENGINE == cm.database_config['db_engine'].upper():
                        url.text = url.text.replace(url.text, cm.database_config[
                            'url'] + "/" + database_name + "?autoReconnect=true&useSSL=false&requireSSL=false&"
                                                           "verifyServerCertificate=false")
                        user.text = user.text.replace(user.text, cm.database_config['user'])
                    elif ORACLE_DB_ENGINE == cm.database_config['db_engine'].upper():
                        url.text = url.text.replace(url.text, cm.database_config['url'] + "/" + DEFAULT_ORACLE_SID)
                        user.text = user.text.replace(user.text, database_name)
                        validation_query.text = validation_query.text.replace(validation_query.text,
                                                                              "SELECT 1 FROM DUAL")
                    elif MSSQL_DB_ENGINE == cm.database_config['db_engine'].upper():
                        url.text = url.text.replace(url.text,
                                                    cm.database_config['url'] + ";" + "databaseName=" + database_name)
                        user.text = user.text.replace(user.text, cm.database_config['user'])
                    else:
                        url.text = url.text.replace(url.text, cm.database_config['url'] + "/" + database_name)
                        user.text = user.text.replace(user.text, cm.database_config['user'])
                    password.text = password.text.replace(password.text, cm.database_config['password'])
                    drive_class_name.text = drive_class_name.text.replace(drive_class_name.text,
                                                                          cm.database_config['driver_class_name'])
                    database_names.append(database_name)
        artifact_tree.write(file_path)


#TODO: Improve the method in generic way to support all products
def save_log_files():
    log_storage = Path(cm.workspace + "/" + LOG_STORAGE)
    if not Path.exists(log_storage):
        Path(log_storage).mkdir(parents=True, exist_ok=True)
    log_file_paths = ARTIFACT_REPORTS_PATHS[cm.product_id]
    if log_file_paths:
        for file in log_file_paths:
            absolute_file_path = Path(cm.workspace + "/" + cm.product_id + "/" + file)
            if Path.exists(absolute_file_path):
                cm.copy_file(absolute_file_path, log_storage)
            else:
                logger.error("File doesn't contain in the given location: " + str(absolute_file_path))


#TODO: Improve the method in generic way to support all products
def save_test_output():
    report_folder = Path(cm.workspace + "/" + TEST_OUTPUT_DIR_NAME)
    if Path.exists(report_folder):
        shutil.rmtree(report_folder)
    report_file_paths = ARTIFACT_REPORTS_PATHS[cm.product_id]
    for key, value in report_file_paths.items():
        for file in value:
            absolute_file_path = Path(cm.workspace + "/" + cm.product_id + "/" + file)
            if Path.exists(absolute_file_path):
                report_storage = Path(cm.workspace + "/" + TEST_OUTPUT_DIR_NAME + "/" + key)
                cm.copy_file(absolute_file_path, report_storage)
                logger.info("Report successfully copied")
            else:
                logger.error("File doesn't contain in the given location: " + str(absolute_file_path))


#TODO: Improve the method in generic way to support all products
# def set_custom_testng():
#     if use_custom_testng_file == "TRUE":
#         testng_source = Path(workspace + "/" + "testng.xml")
#         testng_destination = Path(workspace + "/" + product_id + "/" + TESTNG_DIST_XML_PATH)
#         testng_server_mgt_source = Path(workspace + "/" + "testng-server-mgt.xml")
#         testng_server_mgt_destination = Path(workspace + "/" + product_id + "/" + TESTNG_SERVER_MGT_DIST)
#         # replace testng source
#         replace_file(testng_source, testng_destination)
#         # replace testng server mgt source
# replace_file(testng_server_mgt_source, testng_server_mgt_destination)


def configure_product():
    try:
        global datasource_paths
        global target_dir_abs_path
        global storage_dist_abs_path
        global pom_file_paths

        datasource_paths = DATASOURCE_PATHS[cm.product_id]
        zip_name = dist_name + ZIP_FILE_EXTENSION

        storage_dir_abs_path = Path(cm.workspace + "/" + PRODUCT_STORAGE_DIR_NAME)
        target_dir_abs_path = Path(cm.workspace + "/" + cm.product_id + "/" + DISTRIBUTION_PATH[cm.product_id])
        storage_dist_abs_path = Path(storage_dir_abs_path / dist_name)
        storage_zip_abs_path = Path(storage_dir_abs_path / zip_name)
        configured_dist_storing_loc = Path(target_dir_abs_path / dist_name)
        script_name = Path(WSO2SERVER)
        script_path = Path(storage_dist_abs_path / script_name)

        cm.extract_product(storage_dir_abs_path, storage_zip_abs_path)
        cm.attach_jolokia_agent(script_path)
        cm.copy_jar_file(Path(cm.database_config['sql_driver_location']), Path(storage_dist_abs_path / LIB_PATH))
        if datasource_paths is not None:
            modify_datasources()
        else:
            logger.info("Datasource paths are not defined in the config file")
        os.remove(str(storage_zip_abs_path))
        cm.compress_distribution(configured_dist_storing_loc, storage_dir_abs_path)
        add_distribution_to_m2(storage_dir_abs_path, dist_name, cm.product_version)
        shutil.rmtree(configured_dist_storing_loc, onerror=cm.on_rm_error)
        return database_names
    except FileNotFoundError as e:
        logger.error("Error occurred while finding files", exc_info=True)
    except IOError as e:
        logger.error("Error occurred while accessing files", exc_info=True)
    except Exception as e:
        logger.error("Error occurred while configuring the product", exc_info=True)


def main():
    try:
        global logger
        global dist_name
        logger = cm.function_logger(logging.DEBUG, logging.DEBUG)
        if sys.version_info < (3, 6):
            raise Exception(
                "To run run-intg-test.py script you must have Python 3.6 or latest. Current version info: " + sys.version_info)
        cm.read_property_files()
        if not cm.validate_property_readings():
            raise Exception(
                "Property file doesn't have mandatory key-value pair. Please verify the content of the property file "
                "and the format")

        # get properties assigned to local variables
        pom_path = DIST_POM_PATH[cm.product_id]
        engine = cm.db_engine.upper()
        db_meta_data = get_db_meta_data(engine)
        distribution_path = DISTRIBUTION_PATH[cm.product_id]

        # construct the DB configurations
        cm.construct_db_config(db_meta_data)

        # clone the repository
        cm.clone_repo()

        if cm.test_mode == "RELEASE":
            cm.checkout_to_tag()
            # product name retrieve from product pom files
            dist_name = cm.get_dist_name(pom_path)
            cm.get_latest_released_dist()
        elif cm.test_mode == "SNAPSHOT":
            # product name retrieve from product pom files
            dist_name = cm.get_dist_name(pom_path)
            cm.build_snapshot_dist(distribution_path)
        elif cm.test_mode == "WUM":
            # todo after identify specific steps that are related to WUM, add them to here
            # product name retrieve from product pom files
            dist_name = cm.get_dist_name(pom_path)
            logger.info("WUM specific steps are empty")

        # populate databases
        db_names = configure_product()
        logger.info("================db names : " + str(db_names))
        if db_names is None or not db_names:
            raise Exception("Failed the product configuring")
        cm.setup_databases(db_names, db_meta_data)

        # run integration tests
        if cm.product_id == "product-apim":
            module_path = Path(cm.workspace + "/" + cm.product_id + "/" + 'modules/api-import-export')
            cm.build_module(module_path)
        intg_module_path = Path(cm.workspace + "/" + cm.product_id + "/" + INTEGRATION_PATH[cm.product_id])
        cm.build_module(intg_module_path)
        save_test_output()
        cm.create_output_property_fle()
    except Exception as e:
        logger.error("Error occurred while running the run-intg.py script", exc_info=True)
    except BaseException as e:
        logger.error("Error occurred while doing the configuration", exc_info=True)

if __name__ == "__main__":
    main()