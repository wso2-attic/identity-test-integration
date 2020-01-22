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
import toml
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
import os

from prod_test_constant import DB_META_DATA, DIST_POM_PATH, INTEGRATION_PATH, DISTRIBUTION_PATH, \
    DATASOURCE_PATHS, LIB_PATH, WSO2SERVER, M2_PATH, ARTIFACT_REPORTS_PATHS, POM_FILE_PATHS

from intg_test_constant import NS, ZIP_FILE_EXTENSION, CARBON_NAME, VALUE_TAG, SURFACE_PLUGIN_ARTIFACT_ID, \
    DEPLOYMENT_PROPERTY_FILE_NAME, LOG_FILE_NAME, PRODUCT_STORAGE_DIR_NAME, \
    DEFAULT_DB_USERNAME, LOG_STORAGE, TEST_OUTPUT_DIR_NAME, DEFAULT_ORACLE_SID, MYSQL_DB_ENGINE, \
    ORACLE_DB_ENGINE, PRODUCT_STORAGE_DIR_NAME, MSSQL_DB_ENGINE

database_names = []
db_engine = None
sql_driver_location = None
identity_db_url = None
identity_db_username = None
identity_db_password =  None
identity_db_driver = None
shared_db_url = None
shared_db_username = None
shared_db_password =  None
shared_db_driver = None
identity_db = "WSO2_IDENTITY_DB"
shared_db = "WSO2_SHARED_DB"
def get_db_meta_data(argument):
    switcher = DB_META_DATA
    return switcher.get(argument, False)

def add_environmental_variables():
    if MYSQL_DB_ENGINE == cm.database_config['db_engine'].upper():
        identity_url = cm.database_config[
            'url'] + "/" + identity_db + "?useSSL=false&amp;autoReconnect=true&amp;requireSSL=false" \
                                         "&amp;verifyServerCertificate=false"
        shared_url = cm.database_config[
                           'url'] + "/" + shared_db + \
                     "?useSSL=false&amp;autoReconnect=true&amp;requireSSL=false" \
                     "&amp;verifyServerCertificate=false"
        user = cm.database_config['user']
    elif ORACLE_DB_ENGINE == cm.database_config['db_engine'].upper():
        identity_url= cm.database_config['url'] + "/" + DEFAULT_ORACLE_SID
        shared_url= cm.database_config['url'] + "/" + DEFAULT_ORACLE_SID
        user = cm.database_config['user']
    elif MSSQL_DB_ENGINE == cm.database_config['db_engine'].upper():
        identity_url = cm.database_config['url'] + ";" + "databaseName=" + identity_db
        shared_url = cm.database_config['url'] + ";" + "databaseName=" + shared_db
        user = cm.database_config['user']
    else:
        shared_url = cm.database_config['url'] + "/" + shared_db
        identity_url = cm.database_config['url'] + "/" + identity_db
        user = cm.database_config['user']
    password =  cm.database_config['password']
    driver_class_name = cm.database_config['driver_class_name']

    os.environ["SHARED_DATABASE_URL"] = shared_url
    os.environ["SHARED_DATABASE_USERNAME"] = user
    os.environ["SHARED_DATABASE_PASSWORD"] = password
    os.environ["SHARED_DATABASE_DRIVER"] = driver_class_name
    os.environ["IDENTITY_DATABASE_URL"] = identity_url
    os.environ["IDENTITY_DATABASE_USERNAME"] = user
    os.environ["IDENTITY_DATABASE_PASSWORD"] = password
    os.environ["IDENTITY_DATABASE_DRIVER"] = driver_class_name
    logger.info("Added environmental variables for integration test")


def modify_datasources():
        file_path = Path(storage_dist_abs_path / datasource_path)
        if sys.platform.startswith('win'):
            file_path = cm.winapi_path(file_path)
        logger.info("Modifying datasource: " + str(file_path))
        deployment_toml_config = toml.load(file_path)
        logger.info("loading dep,loyment.toml file")
        logger.info(deployment_toml_config)

        for key in deployment_toml_config:
            if key == 'database':
                database_config = deployment_toml_config[key]
                for key in database_config:
                    if key == 'identity_db':
                        identity_db_config = database_config['identity_db']
                        identity_db_config ['url'] = "$env{IDENTITY_DATABASE_URL}"
                        identity_db_config ['username'] = "$env{IDENTITY_DATABASE_USERNAME}"
                        identity_db_config ['password'] = "$env{IDENTITY_DATABASE_PASSWORD}"
                        identity_db_config ['driver'] = "$env{IDENTITY_DATABASE_DRIVER}"
                        database_names.append(identity_db)

                if key == 'shared_db':
                        shared_db_config = database_config['shared_db']
                        shared_db_config ['url'] = "$env{SHARED_DATABASE_URL}"
                        shared_db_config ['username'] = "$env{SHARED_DATABASE_USERNAME}"
                        shared_db_config ['password'] = "$env{SHARED_DATABASE_PASSWORD}"
                        shared_db_config ['driver'] = "$env{SHARED_DATABASE_DRIVER}"
                        database_names.append(shared_db)

        with open(file_path, 'w') as writer:
            writer.write(toml.dumps(deployment_toml_config))

# Since we have added a method to clone a given git branch and checkout to the latest released tag it is not required to
# modify pom files. Hence in the current implementation this method is not using.
# However, in order to execute this method you can define pom file paths in const_<prod>.py as a constant
# and import it to run-intg-test.py. Thereafter assign it to global variable called pom_file_paths in the
# configure_product method and call the modify_pom_files method.
def modify_pom_files():
    for pom in POM_FILE_PATHS:
        file_path = Path(cm.workspace + "/" + cm.product_id + "/" + pom)
        if sys.platform.startswith('win'):
            file_path = cm.winapi_path(file_path)
        logger.info("Modifying pom file: " + str(file_path))
        ET.register_namespace('', NS['d'])
        artifact_tree = ET.parse(file_path)
        artifarct_root = artifact_tree.getroot()
        data_sources = artifarct_root.find('d:build', NS)
        plugins = data_sources.find('d:plugins', NS)
        for plugin in plugins.findall('d:plugin', NS):
            artifact_id = plugin.find('d:artifactId', NS)
            if artifact_id is not None and artifact_id.text == SURFACE_PLUGIN_ARTIFACT_ID:
                configuration = plugin.find('d:configuration', NS)
                system_properties = configuration.find('d:systemProperties', NS)
                for neighbor in system_properties.iter('{' + NS['d'] + '}' + CARBON_NAME):
                    neighbor.text = cm.modify_distribution_name(neighbor)
                for prop in system_properties:
                    name = prop.find('d:name', NS)
                    if name is not None and name.text == CARBON_NAME:
                        for data in prop:
                            if data.tag == VALUE_TAG:
                                data.text = cm.modify_distribution_name(data)
                break
        artifact_tree.write(file_path)


#TODO: Improve the method in generic way to support all products
def save_log_files():
    log_storage = Path(cm.workspace + "/" + LOG_STORAGE)
    if not Path.exists(log_storage):
        Path(log_storage).mkdir(parents=True, exist_ok=True)
    log_file_paths = ARTIFACT_REPORTS_PATHS
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
    logger.info(str(report_folder))
    if Path.exists(report_folder):
        shutil.rmtree(report_folder)
    logger.info(str(ARTIFACT_REPORTS_PATHS))
    logger.info(str(type(ARTIFACT_REPORTS_PATHS)))
    report_file_paths = ARTIFACT_REPORTS_PATHS
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
#     if cm.use_custom_testng_file == "TRUE":
#         testng_source = Path(cm.workspace + "/" + "testng.xml")
#         testng_destination = Path(cm.workspace + "/" + cm.product_id + "/" + TESTNG_DIST_XML_PATHS)
#         testng_server_mgt_source = Path(cm.workspace + "/" + "testng-server-mgt.xml")
#         testng_server_mgt_destination = Path(cm.workspace + "/" + cm.product_id + "/" + TESTNG_SERVER_MGT_DIST)
#         # replace testng source
#         cm.replace_file(testng_source, testng_destination)
#         # replace testng server mgt source
#         cm.replace_file(testng_server_mgt_source, testng_server_mgt_destination)


def configure_product():
    try:
        global datasource_path
        global target_dir_abs_path
        global storage_dist_abs_path
        global pom_file_paths

        datasource_path = DATASOURCE_PATHS
        zip_name = dist_name + ZIP_FILE_EXTENSION

        storage_dir_abs_path = Path(cm.workspace + "/" + PRODUCT_STORAGE_DIR_NAME)
        target_dir_abs_path = Path(cm.workspace + "/" + cm.product_id + "/" + DISTRIBUTION_PATH)
        storage_dist_abs_path = Path(storage_dir_abs_path / dist_name)
        storage_zip_abs_path = Path(storage_dir_abs_path / zip_name)
        configured_dist_storing_loc = Path(target_dir_abs_path / dist_name)
        script_name = Path(WSO2SERVER)

        script_path = Path(storage_dist_abs_path / script_name)
        cm.extract_product(storage_dir_abs_path, storage_zip_abs_path)
        cm.attach_jolokia_agent(script_path)
        cm.copy_jar_file(Path(cm.database_config['sql_driver_location']), Path(storage_dist_abs_path / LIB_PATH))
        if datasource_path is not None:
            modify_datasources()
        else:
            logger.info("Datasource paths are not defined in the config file")
        os.remove(str(storage_zip_abs_path))
        cm.compress_distribution(configured_dist_storing_loc, storage_dir_abs_path)
        cm.add_distribution_to_m2(storage_dir_abs_path, M2_PATH)
        shutil.rmtree(configured_dist_storing_loc, onerror=cm.on_rm_error)
        return database_names
    except FileNotFoundError as e:
        logger.error("Error occurred while finding files", exc_info=True)
    except IOError as e:
        logger.error("Error occurred while accessing files", exc_info=True)
    except Exception as e:
        logger.error("Error occurred while configuring the product", exc_info=True)


def build_source_without_tests(source_path):
    """Build the product-source.
    """
    logger.info('Building the source skipping tests')
    if sys.platform.startswith('win'):
        subprocess.call(['mvn', 'clean', 'install', '-B', '-e','-Dmaven.test.skip=true'], shell=True, cwd=source_path)
    else:
        subprocess.call(['mvn', 'clean', 'install', '-B', '-e', '-Dmaven.test.skip=true'], cwd=source_path)
    logger.info('Module build is completed. Module: ' + str(source_path))

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
        pom_path = DIST_POM_PATH
        engine = cm.db_engine.upper()
        db_meta_data = get_db_meta_data(engine)
        distribution_path = DISTRIBUTION_PATH

        # construct the database configurations
        cm.construct_db_config(db_meta_data)

        # clone the repository
        cm.clone_repo()

        if cm.test_mode == "RELEASE":
            cm.checkout_to_tag()
            # product name retrieve from product pom files
            dist_name = cm.get_dist_name(pom_path)
            # build the product without test once to make samples and required artifacts to be available.
            build_source_without_tests(cm.workspace + "/" + cm.product_id + "/")
            cm.get_latest_released_dist()
        elif cm.test_mode == "SNAPSHOT":
            # product name retrieve from product pom files
            dist_name = cm.get_dist_name(pom_path)
            cm.build_snapshot_dist(distribution_path)
        elif cm.test_mode == "WUM":
            dist_name = cm.get_dist_name_wum()

        # populate databases
        db_names = configure_product()
        if db_names is None or not db_names:
            raise Exception("Failed the product configuring")
        cm.setup_databases(db_names, db_meta_data)
        # run integration tests
        # Buld Common module
        add_environmental_variables()
        module_path = Path(cm.workspace + "/" + cm.product_id + "/" + 'modules/integration/tests-common')
        logger.info('Building common module. Build path: '+ str(module_path) + ' \n')

        cm.build_module(module_path)
        intg_module_path = Path(cm.workspace + "/" + cm.product_id + "/" + INTEGRATION_PATH)
        logger.info('Building integration module. Build path: '+ str(intg_module_path) + ' \n')
        cm.build_module(intg_module_path)
        save_test_output()
        cm.create_output_property_fle()
    except Exception as e:
        logger.error("Error occurred while running the run-intg-test.py script", exc_info=True)
    except BaseException as e:
        logger.error("Error occurred while doing the configuration", exc_info=True)


if __name__ == "__main__":
    main()
