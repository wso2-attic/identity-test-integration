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
import configure_product as cp
from subprocess import Popen, PIPE
from const import TEST_PLAN_PROPERTY_FILE_NAME, INFRA_PROPERTY_FILE_NAME, LOG_FILE_NAME, DB_META_DATA, \
    PRODUCT_STORAGE_DIR_NAME, DB_CARBON_DB, DB_STAT_DB, DB_PRODUCT_DB, DB_BPS_DB, DB_METRICS_DB, DEFAULT_DB_USERNAME, \
    LOG_STORAGE, LOG_FILE_PATHS, DIST_POM_PATH, NS

git_repo_url = None
git_branch = None
os_type = None
workspace = None
product_name = None
product_zip_name = None
product_id = None
log_file_name = None
target_path = None
db_engine = None
db_engine_version = None
latest_product_release_api = None
latest_product_build_artifacts_api = None
sql_driver_location = None
db_host = None
db_port = None
db_username = None
db_password = None
tag_name = None
test_mode = None
build_from_source = None
database_config = {}
version = None

def read_proprty_files():
    global db_engine
    global db_engine_version
    global git_repo_url
    global git_branch
    global latest_product_release_api
    global latest_product_build_artifacts_api
    global sql_driver_location
    global db_host
    global db_port
    global db_username
    global db_password
    global workspace
    global product_id
    global database_config
    global test_mode
    global build_from_source

    workspace = os.getcwd()
    property_file_paths = []
    test_plan_prop_path = Path(workspace + "/" + TEST_PLAN_PROPERTY_FILE_NAME)
    infra_prop_path = Path(workspace + "/" + INFRA_PROPERTY_FILE_NAME)

    if Path.exists(test_plan_prop_path) and Path.exists(infra_prop_path):
        property_file_paths.append(test_plan_prop_path)
        property_file_paths.append(infra_prop_path)

        for path in property_file_paths:
            with open(path, 'r') as filehandle:
                for line in filehandle:
                    if line.startswith("#"):
                        continue
                    prop = line.split("=")
                    key = prop[0]
                    val = prop[1]
                    if key == "DBEngine":
                        db_engine = val.strip()
                    elif key == "DBEngineVersion":
                        db_engine_version = val
                    elif key == "PRODUCT_GIT_URL":
                        git_repo_url = val.strip().replace('\\', '')
                        product_id = git_repo_url.split("/")[-1].split('.')[0]
                    elif key == "PRODUCT_GIT_BRANCH":
                        git_branch = val.strip()
                    elif key == "LATEST_PRODUCT_RELEASE_API":
                        latest_product_release_api = val.strip().replace('\\', '')
                    elif key == "LATEST_PRODUCT_BUILD_ARTIFACTS_API":
                        latest_product_build_artifacts_api = val.strip().replace('\\', '')
                    elif key == "SQL_DRIVERS_LOCATION_UNIX" and not sys.platform.startswith('win'):
                        sql_driver_location = val.strip()
                    elif key == "SQL_DRIVERS_LOCATION_WINDOWS" and sys.platform.startswith('win'):
                        sql_driver_location = val.strip()
                    elif key == "DatabaseHost":
                        db_host = val.strip()
                    elif key == "DatabasePort":
                        db_port = val.strip()
                    elif key == "DBUsername":
                        db_username = val.strip()
                    elif key == "DBPassword":
                        db_password = val.strip()
                    elif key == "TEST_MODE":
                        test_mode = val.strip()
                    elif key == "BUILD_FROM_SOURCE":
                        build_from_source = val.strip()
    else:
        raise Exception("Test Plan Property file or Infra Property file is not in the workspace: " + workspace)


def validate_property_radings():
    missing_values = ""
    if db_engine is None:
        missing_values += " -DBEngine- "
    if git_repo_url is None:
        missing_values += " -PRODUCT_GIT_URL- "
    if product_id is None:
        missing_values += " -product-id- "
    if git_branch is None:
        missing_values += " -PRODUCT_GIT_BRANCH- "
    if latest_product_release_api is None:
        missing_values += " -LATEST_PRODUCT_RELEASE_API- "
    if latest_product_build_artifacts_api is None:
        missing_values += " -LATEST_PRODUCT_BUILD_ARTIFACTS_API- "
    if sql_driver_location is None:
        missing_values += " -SQL_DRIVERS_LOCATION_<OS_Type>- "
    if db_host is None:
        missing_values += " -DatabaseHost- "
    if db_port is None:
        missing_values += " -DatabasePort- "
    if db_password is None:
        missing_values += " -DBPassword- "
    if test_mode is None:
        missing_values += " -TEST_MODE- "

    if missing_values != "":
        logger.error('Invalid property file is found. Missing values: %s ', missing_values)
        return False
    else:
        return True


def get_db_meta_data(argument):
    switcher = DB_META_DATA
    return switcher.get(argument, False)


def construct_url(prefix):
    url = prefix + db_host + ":" + db_port
    return url


def function_logger(file_level, console_level=None):
    global log_file_name
    log_file_name = LOG_FILE_NAME
    function_name = inspect.stack()[1][3]
    logger = logging.getLogger(function_name)
    # By default, logs all messages
    logger.setLevel(logging.DEBUG)

    if console_level != None:
        # StreamHandler logs to console
        ch = logging.StreamHandler()
        ch.setLevel(console_level)
        ch_format = logging.Formatter('%(asctime)s - %(message)s')
        ch.setFormatter(ch_format)
        logger.addHandler(ch)

    # log in to a file
    fh = logging.FileHandler("{0}.log".format(function_name))
    fh.setLevel(file_level)
    fh_format = logging.Formatter('%(asctime)s - %(lineno)d - %(levelname)-8s - %(message)s')
    fh.setFormatter(fh_format)
    logger.addHandler(fh)

    return logger


def download_file(url, destination):
    """Download a file using wget package.
    Download the given file in _url_ as the directory+name provided in _destination_
    """
    logger.info('Downloading file URL: ' + url + ' destination: ' + destination)
    wget.download(url, destination)


def get_db_hostname(url, db_type):
    """Retreive db hostname from jdbc url
    """
    if db_type == 'ORACLE':
        hostname = url.split(':')[3].replace("@", "")
    else:
        hostname = url.split(':')[2].replace("//", "")
    return hostname


def run_sqlserver_commands(query):
    """Run SQL_SERVER commands using sqlcmd utility.
    """
    subprocess.call(
        ['sqlcmd', '-S', db_host, '-U', database_config['user'], '-P', database_config['password'], '-Q', query])


def get_mysql_connection(db_name=None):
    if db_name is not None:
        conn = pymysql.connect(host=get_db_hostname(database_config['url'], 'MYSQL'), user=database_config['user'],
                               passwd=database_config['password'], db=db_name)
    else:
        conn = pymysql.connect(host=get_db_hostname(database_config['url'], 'MYSQL'), user=database_config['user'],
                               passwd=database_config['password'])
    return conn


def run_mysql_commands(query):
    """Run mysql commands using mysql client when db name not provided.
    """
    conn = get_mysql_connection()
    conectr = conn.cursor()
    conectr.execute(query)
    conn.close()


def get_ora_user_carete_query(database):
    query = "CREATE USER {0} IDENTIFIED BY {1};".format(
        database, database_config["password"])
    return query


def get_ora_grant_query(database):
    query = "GRANT CONNECT, RESOURCE, DBA TO {0};".format(
        database)
    return query


def execute_oracle_command(query):
    """Run oracle commands using sqlplus client when db name(user) is not provided.
    """
    connect_string = "{0}/{1}@//{2}/{3}".format(database_config["user"], database_config["password"],
                                                db_host, "ORCL")
    session = Popen(['sqlplus', '-S', connect_string], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    session.stdin.write(bytes(query, 'utf-8'))
    return session.communicate()


def create_oracle_user(database):
    """This method is able to create the user and grant permission to the created user in oracle
    """
    user_creating_query = get_ora_user_carete_query(database)
    logger.info(execute_oracle_command(user_creating_query))
    permission_granting_query = get_ora_grant_query(database)
    return execute_oracle_command(permission_granting_query)


def run_oracle_script(script, database):
    """Run oracle commands using sqlplus client when dbname(user) is provided.
    """
    connect_string = "{0}/{1}@//{2}/{3}".format(database, database_config["password"],
                                                db_host, "ORCL")
    session = Popen(['sqlplus', '-S', connect_string], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    session.stdin.write(bytes(script, 'utf-8'))
    return session.communicate()


def run_sqlserver_script_file(db_name, script_path):
    """Run SQL_SERVER script file on a provided database.
    """
    subprocess.call(
        ['sqlcmd', '-S', db_host, '-U', database_config["user"], '-P', database_config["password"], '-d', db_name, '-i',
         script_path])


def run_mysql_script_file(db_name, script_path):
    """Run MYSQL db script file on a provided database.
    """
    conn = get_mysql_connection(db_name)
    connector = conn.cursor()

    sql = open(script_path).read()
    sql_parts = sqlparse.split(sql)
    for sql_part in sql_parts:
        if sql_part.strip() == '':
            continue
        connector.execute(sql_part)
    conn.close()


def copy_file(source, target):
    """Copy the source file to the target.
    """
    if sys.platform.startswith('win'):
        source = cp.winapi_path(source)
        target = cp.winapi_path(target)
        shutil.copy(source, target)
    else:
        shutil.copy(source, target)


def get_product_name():
    """Get the product name by reading root pom.
    """
    global product_name
    global product_zip_name
    global version
    dist_pom_path = Path(workspace + "/" + product_id + "/" + DIST_POM_PATH[product_id])
    if sys.platform.startswith('win'):
        dist_pom_path = cp.winapi_path(dist_pom_path)
    ET.register_namespace('', NS['d'])
    artifact_tree = ET.parse(dist_pom_path)
    artifact_root = artifact_tree.getroot()
    parent = artifact_root.find('d:parent', NS)
    artifact_id = artifact_root.find('d:artifactId', NS)
    version = parent.find('d:version', NS).text
    product_name = artifact_id.text + "-" + version
    product_zip_name = product_name + ".zip"
    return product_name


def setup_databases(script_path, db_names):
    """Create required databases.
    """
    for database in db_names:
        if database == DB_CARBON_DB:
            if db_engine.upper() == 'SQLSERVER-SE':
                # create database
                run_sqlserver_commands('CREATE DATABASE {0}'.format(database))
                # manipulate script path
                scriptPath = script_path / 'mssql.sql'

                # manipulate conent script path
                scriptPathConsent = script_path / 'consent/mssql.sql'
                # run db scripts
                run_sqlserver_script_file(database, str(scriptPath))
                run_sqlserver_script_file(database, str(scriptPathConsent))
            elif db_engine.upper() == 'MYSQL':
                scriptPath = script_path / 'mysql5.7.sql'
                # manipulate conent script path
                scriptPathConsent = script_path / 'consent/mysql-5.7.sql'
                # create database
                run_mysql_commands('CREATE DATABASE IF NOT EXISTS {0};'.format(database))
                # run db script
                run_mysql_script_file(database, str(scriptPath))
                run_mysql_script_file(database, str(scriptPathConsent))

            elif db_engine.upper() == 'ORACLE-SE2':
                # create oracle schema
                logger.info(create_oracle_user(database))
                # run db script
                scriptPath = script_path / 'oracle.sql'
                # manipulate conent script path
                scriptPathConsent = script_path / 'consent/oracle.sql'
                logger.info(run_oracle_script('@{0}'.format(str(scriptPath)), database))
                logger.info(run_oracle_script('@{0}'.format(str(scriptPathConsent)), database))
        elif database == DB_PRODUCT_DB[product_id]:
            if db_engine.upper() == 'SQLSERVER-SE':
                # create database
                run_sqlserver_commands('CREATE DATABASE {0}'.format(database))
                # manipulate script path
                scriptPath = script_path / 'identity/mssql.sql'
                # run db scripts
                run_sqlserver_script_file(database, str(scriptPath))
            elif db_engine.upper() == 'MYSQL':
                scriptPath = script_path / 'identity/mysql5.7.sql'
                # create database
                run_mysql_commands('CREATE DATABASE IF NOT EXISTS {0};'.format(database))
                # run db script
                run_mysql_script_file(database, str(scriptPath))
            elif db_engine.upper() == 'ORACLE-SE2':
                logger.info(create_oracle_user(database))
                # run db script
                scriptPath = script_path / 'identity/oracle.sql'
                logger.info(run_oracle_script('@{0}'.format(str(scriptPath)), database))
        elif database == DB_STAT_DB:
            if db_engine.upper() == 'SQLSERVER-SE':
                # create database
                run_sqlserver_commands('CREATE DATABASE {0}'.format(database))
            elif db_engine.upper() == 'MYSQL':
                # create database
                run_mysql_commands('CREATE DATABASE IF NOT EXISTS {0};'.format(database))
            elif db_engine.upper() == 'ORACLE-SE2':
                # create database
                logger.info(create_oracle_user(database))
        elif database == DB_BPS_DB:
            if db_engine.upper() == 'SQLSERVER-SE':
                # create database
                run_sqlserver_commands('CREATE DATABASE {0}'.format(database))
                # manipulate script path
                scriptPath = script_path / 'bps/bpel/create/mssql.sql'
                # run db scripts
                run_sqlserver_script_file(database, str(scriptPath))
            elif db_engine.upper() == 'MYSQL':
                # create database
                run_mysql_commands('CREATE DATABASE IF NOT EXISTS {0};'.format(database))
                # manipulate script path
                scriptPath = script_path / 'bps/bpel/create/mysql.sql'
                # run db scripts
                run_mysql_script_file(database, str(scriptPath))
            elif db_engine.upper() == 'ORACLE-SE2':
                logger.info(create_oracle_user(database))
                # run db script
                scriptPath = script_path / 'bps/bpel/create/oracle.sql'
                logger.info(run_oracle_script('@{0}'.format(str(scriptPath)), database))
        elif database == DB_METRICS_DB:
            if db_engine.upper() == 'SQLSERVER-SE':
                # create database
                run_sqlserver_commands('CREATE DATABASE {0}'.format(database))
                # manipulate script path
                scriptPath = script_path / 'metrics/mssql.sql'
                # run db scripts
                run_sqlserver_script_file(database, str(scriptPath))
            elif db_engine.upper() == 'MYSQL':
                scriptPath = script_path / 'metrics/mysql.sql'
                # create database
                run_mysql_commands('CREATE DATABASE IF NOT EXISTS {0};'.format(database))
                # run db script
                run_mysql_script_file(database, str(scriptPath))
            elif db_engine.upper() == 'ORACLE-SE2':
                logger.info(create_oracle_user(database))
                # run db script
                scriptPath = script_path / 'metrics/oracle.sql'
                logger.info(run_oracle_script('@{0}'.format(str(scriptPath)), database))


def construct_db_config():
    """Use properties which are get by reading property files and construct the database config object which will use
    when configuring the databases.
    """
    db_meta_data = get_db_meta_data(db_engine.upper())
    if db_meta_data:
        database_config["driver_class_name"] = db_meta_data["driverClassName"]
        database_config["password"] = db_password
        database_config["sql_driver_location"] = sql_driver_location + "/" + db_meta_data["jarName"]
        database_config["url"] = construct_url(db_meta_data["prefix"])
        database_config["db_engine"] = db_engine
        if db_username is None:
            database_config["user"] = DEFAULT_DB_USERNAME
        else:
            database_config["user"] = db_username

    else:
        raise BaseException(
            "DB config parsing is failed. DB engine name in the property file doesn't match with the constant: " + str(
                db_engine.upper()))


def run_integration_test():
    """Run integration tests.
    """
    integration_tests_path = Path(workspace + "/" + product_id + "/" + 'modules/integration')
    if sys.platform.startswith('win'):
        subprocess.call(['mvn', 'clean', 'install', '-B',
                         '-Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn'],
                        shell=True, cwd=integration_tests_path)
    else:
        subprocess.call(['mvn', 'clean', 'install', '-B',
                         '-Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn'],
                        cwd=integration_tests_path)
    logger.info('Integration test Running is completed.')

def save_log_files():
    log_storage = Path(workspace + "/" + LOG_STORAGE)
    if not Path.exists(log_storage):
        Path(log_storage).mkdir(parents=True, exist_ok=True)
    log_file_paths = LOG_FILE_PATHS[product_id]
    if log_file_paths:
        for file in log_file_paths:
            absolute_file_path = Path(workspace + "/" + product_id + "/" + file)
            if Path.exists(absolute_file_path):
                copy_file(absolute_file_path, log_storage)
            else:
                logger.error("File doesn't contain in the given location: " + str(absolute_file_path))


def clone_repo():
    """Clone the product repo
    """
    try:
        global tag_name
        logger.info('cloning '+ git_repo_url + '@' + git_branch)
        subprocess.call(['git', 'clone', '--branch', git_branch, git_repo_url], cwd=workspace)
        logger.info('product repository cloning is done.')
    except Exception as e:
        logger.error("Error occurred while cloning the product repo: ", exc_info=True)


def checkout_to_tag(name):
    """Checkout to the given tag
    """
    try:
        git_path = Path(workspace + "/" + product_id)
        tag = "tags/" + name
        subprocess.call(["git", "fetch", "origin", tag], cwd=git_path)
        subprocess.call(["git", "checkout", "-B", tag, name], cwd=git_path)
        logger.info('checkout to the branch: ' + tag)
    except Exception as e:
        logger.error("Error occurred while cloning the product repo and checkout to the latest tag of the branch",
                     exc_info=True)


def get_latest_tag_name(product):
    """Get the latest tag name from git location
    """
    global tag_name
    git_path = Path(workspace + "/" + product)
    binary_val_of_tag_name = subprocess.Popen(["git", "describe", "--abbrev=0", "--tags"],
                                              stdout=subprocess.PIPE, cwd=git_path)
    tag_name = binary_val_of_tag_name.stdout.read().strip().decode("utf-8")
    return tag_name


def get_product_file_path():
    """Get the latest tag name from git location
    """
    # product download path and file name constructing
    product_download_dir = Path(workspace + "/" + PRODUCT_STORAGE_DIR_NAME)
    if not Path.exists(product_download_dir):
        Path(product_download_dir).mkdir(parents=True, exist_ok=True)
    return product_download_dir / product_zip_name


def get_relative_path_of_dist_storage(xml_path):
    """Get the relative path of distribution storage
    """
    dom = minidom.parse(urllib2.urlopen(xml_path))  # parse the data
    artifact_elements = dom.getElementsByTagName('artifact')

    for artifact in artifact_elements:
        file_name_elements = artifact.getElementsByTagName("fileName")
        for file_name in file_name_elements:
            if file_name.firstChild.nodeValue == product_zip_name:
                parent_node = file_name.parentNode
                return parent_node.getElementsByTagName("relativePath")[0].firstChild.nodeValue
    return None


def get_latest_released_dist():
    """Get the latest released distribution
    """
    # construct the distribution downloading url
    relative_path = get_relative_path_of_dist_storage(latest_product_release_api + "xml")
    if relative_path is None:
        raise Exception("Error occured while getting relative path")
    dist_downl_url = latest_product_release_api.split('/api')[0] + "/artifact/" + relative_path
    # download the last released pack from Jenkins
    download_file(dist_downl_url, str(get_product_file_path()))
    logger.info('downloading the latest released pack from Jenkins is completed.')


def get_latest_stable_artifacts_api():
    """Get the API of the latest stable artifacts
    """
    dom = minidom.parse(urllib2.urlopen(latest_product_build_artifacts_api + "xml"))
    main_artifact_elements = dom.getElementsByTagName('mainArtifact')

    for main_artifact in main_artifact_elements:
        canonical_name_elements = main_artifact.getElementsByTagName("canonicalName")
        for canonical_name in canonical_name_elements:
            if canonical_name.firstChild.nodeValue == product_name + ".pom":
                parent_node = main_artifact.parentNode
                return parent_node.getElementsByTagName("url")[0].firstChild.nodeValue
    return None


def get_latest_stable_dist():
    """Download the latest stable distribution
    """
    build_num_artifact = get_latest_stable_artifacts_api()
    build_num_artifact = re.sub(r'http.//(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})', "https://wso2.org", build_num_artifact)
    if build_num_artifact is None:
        raise Exception("Error occured while getting latest stable build artifact API path")
    relative_path = get_relative_path_of_dist_storage(build_num_artifact + "api/xml")
    if relative_path is None:
        raise Exception("Error occured while getting relative path")
    dist_downl_url = build_num_artifact + "artifact/" + relative_path
    download_file(dist_downl_url, str(get_product_file_path()))
    logger.info('downloading the latest stable pack from Jenkins is completed.')


def create_output_property_fle():
    """Create output property file which is used when generating email
    """
    output_property_file = open("output.properties", "w+")
    git_url = git_repo_url + "/tree/" + git_branch
    output_property_file.write("GIT_LOCATION=%s\r\n" % git_url)
    output_property_file.write("GIT_REVISION=%s\r\n" % tag_name)
    output_property_file.close()


def replace_file(source, destination):
    """Replace source file to the destination
    """
    logger.info('replacing files from:' + str(source) + "to: " + str(destination))
    if sys.platform.startswith('win'):
        source = cp.winapi_path(source)
        destination = cp.winapi_path(destination)
    shutil.move(source, destination)

def build_source(source_path):
    """Build the product-source.
    """
    logger.info('Building the source skipping tests')
    if sys.platform.startswith('win'):
        subprocess.call(['mvn', 'clean', 'install', '-B', '-e',
                         '-Dmaven.test.skip=true'],
                        shell=True, cwd=source_path)
    else:
        subprocess.call(['mvn', 'clean', 'install', '-B', '-e',
                         '-Dmaven.test.skip=true'],
                        cwd=source_path)
    logger.info('Module build is completed. Module: ' + str(source_path))


def main():
    try:
        global logger
        global product_name
        logger = function_logger(logging.DEBUG, logging.DEBUG)
        if sys.version_info < (3, 6):
            raise Exception(
                "To run run-intg-test.py script you must have Python 3.6 or latest. Current version info: " + sys.version_info)
        read_proprty_files()
        if not validate_property_radings():
            raise Exception(
                "Property file doesn't have mandatory key-value pair. Please verify the content of the property file "
                "and the format")
        construct_db_config()

        # clone the repository
        clone_repo()

        if test_mode == "DEBUG":
            checkout_to_tag(get_latest_tag_name(product_id))
            # product name retrieve from product pom files
            product_name = get_product_name()
            get_latest_released_dist()
            testng_source = Path(workspace + "/" + "testng.xml")
            testng_destination = Path(workspace + "/" + product_id + "/" +
                                      'modules/integration/tests-integration/tests-backend/src/test/resources/testng.xml')
            testng_server_mgt_source = Path(workspace + "/" + "testng-server-mgt.xml")
            testng_server_mgt_destination = Path(workspace + "/" + product_id + "/" +
                                                 'modules/integration/tests-integration/tests-backend/src/test/resources/testng-server-mgt.xml')
            # replace testng source
            replace_file(testng_source, testng_destination)
            # replace testng server mgt source
            replace_file(testng_server_mgt_source, testng_server_mgt_destination)
        elif test_mode == "RELEASE":
            checkout_to_tag(get_latest_tag_name(product_id))
            # product name retrieve from product pom files
            product_name = get_product_name()
            if build_from_source == "TRUE":
                source_path = Path(workspace + "/" + product_id)
                build_source(source_path)
            get_latest_released_dist()
        elif test_mode == "SNAPSHOT":
            # product name retrieve from product pom files
            product_name = get_product_name()
            get_latest_stable_dist()
        elif test_mode == "WUM":
            # todo after identify specific steps that are related to WUM, add them to here
            # product name retrieve from product pom files
            product_name = get_product_name()
            logger.info("WUM specific steps are empty")

        # populate databases
        script_path = Path(workspace + "/" + PRODUCT_STORAGE_DIR_NAME + "/" + product_name + "/" + 'dbscripts')
        db_names = cp.configure_product(product_name, version, product_id, database_config, workspace)
        if db_names is None or not db_names:
            raise Exception("Failed the product configuring")
        setup_databases(script_path, db_names)
        logger.info('Database setting up is done.')
        logger.info('Starting Integration test running.')
        #run integration tests
        run_integration_test()
        save_log_files()
        create_output_property_fle()
    except Exception as e:
        logger.error("Error occurred while running the run-intg.py script", exc_info=True)
    except BaseException as e:
        logger.error("Error occurred while doing the configuration", exc_info=True)


if __name__ == "__main__":
    main()
