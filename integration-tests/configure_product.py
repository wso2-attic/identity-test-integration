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
import argparse as argparse
from xml.etree import ElementTree as ET
from zipfile import ZipFile
import os
import stat
import sys
from pathlib import Path
import shutil
import logging
from const import ZIP_FILE_EXTENSION, NS, SURFACE_PLUGIN_ARTIFACT_ID, CARBON_NAME, VALUE_TAG, \
    DEFAULT_ORACLE_SID, DATASOURCE_PATHS, MYSQL_DB_ENGINE, ORACLE_DB_ENGINE, LIB_PATH, PRODUCT_STORAGE_DIR_NAME, \
    DISTRIBUTION_PATH, MSSQL_DB_ENGINE, WSO2SERVER

datasource_paths = None
database_url = None
database_user = None
database_pwd = None
database_drive_class_name = None
product_name = None
product_version = None
product_home_path = None
distribution_storage = None
database_config = None
product_storage = None
workspace = None
lib_path = None
sql_driver_location = None
product_id = None
database_names = []
pom_file_paths = None

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ZipFileLongPaths(ZipFile):
    def _extract_member(self, member, targetpath, pwd):
        targetpath = winapi_path(targetpath)
        return ZipFile._extract_member(self, member, targetpath, pwd)


def winapi_path(dos_path, encoding=None):
    path = os.path.abspath(dos_path)

    if path.startswith("\\\\"):
        path = "\\\\?\\UNC\\" + path[2:]
    else:
        path = "\\\\?\\" + path

    return path


def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def extract_product(path):
    if Path.exists(path):
        logger.info("Extracting the product  into " + str(product_storage))
        if sys.platform.startswith('win'):
            with ZipFileLongPaths(path, "r") as zip_ref:
                zip_ref.extractall(product_storage)
        else:
            with ZipFile(str(path), "r") as zip_ref:
                zip_ref.extractall(product_storage)
    else:
        raise FileNotFoundError("File is not found to extract, file path: " + str(path))


def compress_distribution(distribution_path, root_dir):
    if type(distribution_path) == str:
        distribution_path = Path(distribution_path)
    if not Path.exists(distribution_path):
        Path(distribution_path).mkdir(parents=True, exist_ok=True)

    shutil.make_archive(distribution_path, "zip", root_dir)


def copy_jar_file(source, destination):
    logger.info('sql driver is coping to the product lib folder')
    if sys.platform.startswith('win'):
        source = winapi_path(source)
        destination = winapi_path(destination)
    shutil.copy(source, destination)


def modify_distribution_name(element):
    temp = element.text.split("/")
    temp[-1] = product_name + ZIP_FILE_EXTENSION
    return '/'.join(temp)


# Since we have added a method to clone a given git branch and checkout to the latest released tag it is not required to
# modify pom files. Hence in the current implementation this method is not using.
# However, in order to execute this method you can define pom file paths in const.py as a constant
# and import it to configure_product.py. Thereafter assign it to global variable called pom_file_paths in the
# configure_product method and call the modify_pom_files method.
def modify_pom_files():
    for pom in pom_file_paths:
        file_path = Path(workspace + "/" + product_id + "/" + pom)
        if sys.platform.startswith('win'):
            file_path = winapi_path(file_path)
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
                    neighbor.text = modify_distribution_name(neighbor)
                for prop in system_properties:
                    name = prop.find('d:name', NS)
                    if name is not None and name.text == CARBON_NAME:
                        for data in prop:
                            if data.tag == VALUE_TAG:
                                data.text = modify_distribution_name(data)
                break
        artifact_tree.write(file_path)


def attach_jolokia_agent(spath):
    logger.info('attaching jolokia agent as a java agent')
    sp = str(spath)

    if sys.platform.startswith('win'):
        jolokia_agent = \
            "    -javaagent:C:\\testgrid\\jolokia-jvm-1.6.0-agent.jar=port=8778,host=localhost,protocol=http \\\n"
    else:
        jolokia_agent = \
            "    -javaagent:/opt/wso2/jolokia-jvm-1.6.0-agent.jar=port=8778,host=localhost,protocol=http \\\n"

    with open(sp, "r") as in_file:
        buf = in_file.readlines()

    with open(sp, "w") as out_file:
        for line in buf:
            if line == "    $JAVACMD \\\n":
                line = line + jolokia_agent
                logger.info(line)
            out_file.write(line)


def modify_datasources():
    for data_source in datasource_paths:
        file_path = Path(product_home_path / data_source)
        if sys.platform.startswith('win'):
            file_path = winapi_path(file_path)
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
                    if MYSQL_DB_ENGINE == database_config['db_engine'].upper():
                        url.text = url.text.replace(url.text, database_config[
                            'url'] + "/" + database_name + "?autoReconnect=true&useSSL=false&requireSSL=false&"
                                                     "verifyServerCertificate=false")
                        user.text = user.text.replace(user.text, database_config['user'])
                    elif ORACLE_DB_ENGINE == database_config['db_engine'].upper():
                        url.text = url.text.replace(url.text, database_config['url'] + "/" + DEFAULT_ORACLE_SID)
                        user.text = user.text.replace(user.text, database_name)
                        validation_query.text = validation_query.text.replace(validation_query.text,
                                                                              "SELECT 1 FROM DUAL")
                    elif MSSQL_DB_ENGINE == database_config['db_engine'].upper():
                        url.text = url.text.replace(url.text,
                                                    database_config['url'] + ";" + "databaseName=" + database_name)
                        user.text = user.text.replace(user.text, database_config['user'])
                    else:
                        url.text = url.text.replace(url.text, database_config['url'] + "/" + database_name)
                        user.text = user.text.replace(user.text, database_config['user'])
                    password.text = password.text.replace(password.text, database_config['password'])
                    drive_class_name.text = drive_class_name.text.replace(drive_class_name.text,
                                                                          database_config['driver_class_name'])
                    database_names.append(database_name)
        artifact_tree.write(file_path)


def copy_distribution_to_m2(storage, name, version):
    # todo need to generalize this method
    home = Path.home()
    linux_m2_path = home / ".m2/repository/org/wso2/is/wso2is" / version / name
    windows_m2_path = Path(
        "/Documents and Settings/Administrator/.m2/repository/org/wso2/is/wso2is" + "/" + version + "/" + name)
    if sys.platform.startswith('win'):
        windows_m2_path = winapi_path(windows_m2_path)
        storage = winapi_path(storage)
        compress_distribution(windows_m2_path, storage)
        shutil.rmtree(windows_m2_path, onerror=on_rm_error)
    else:
        compress_distribution(linux_m2_path, storage)
        shutil.rmtree(linux_m2_path, onerror=on_rm_error)


def configure_product(product, version, id, db_config, ws):
    logger.info('Configuring product: ' + product)
    try:
        global product_version
        global product_name
        global product_id
        global database_config
        global workspace
        global datasource_paths
        global distribution_storage
        global product_home_path
        global product_storage
        global lib_path
        global pom_file_paths

        product_name = product
        product_id = id
        database_config = db_config
        product_version = version
        workspace = ws
        datasource_paths = DATASOURCE_PATHS[product_id]
        lib_path = LIB_PATH
        product_storage = Path(workspace + "/" + PRODUCT_STORAGE_DIR_NAME)
        distribution_storage = Path(workspace + "/" + product_id + "/" + DISTRIBUTION_PATH[product_id])
        product_home_path = Path(product_storage / product_name)
        zip_name = product_name + ZIP_FILE_EXTENSION
        product_location = Path(product_storage / zip_name)
        configured_product_path = Path(distribution_storage / product_name)
        script_name = Path(WSO2SERVER)
        script_path = Path(product_home_path / script_name)
        logger.info(product_location)
        extract_product(product_location)
        attach_jolokia_agent(script_path)
        copy_jar_file(Path(database_config['sql_driver_location']), Path(product_home_path / lib_path))
        if datasource_paths is not None:
            modify_datasources()
        else:
            logger.info("Datasource paths are not defined in the config file")
        os.remove(str(product_location))
        compress_distribution(configured_product_path, product_storage)
        copy_distribution_to_m2(product_storage, product_name, product_version)
        shutil.rmtree(configured_product_path, onerror=on_rm_error)
        return database_names
    except FileNotFoundError as e:
        logger.error("Error occurred while finding files", exc_info=True)
    except IOError as e:
        logger.error("Error occurred while accessing files", exc_info=True)
    except Exception as e:
        logger.error("Error occurred while configuring the product", exc_info=True)
