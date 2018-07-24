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

NS = {'d': 'http://maven.apache.org/POM/4.0.0'}
ZIP_FILE_EXTENSION = ".zip"
CARBON_NAME = "carbon.zip"
VALUE_TAG = "{http://maven.apache.org/POM/4.0.0}value"
SURFACE_PLUGIN_ARTIFACT_ID = "maven-surefire-plugin"
DATASOURCE_PATHS = {"product-apim": ["repository/conf/datasources/master-datasources.xml",
                                     "repository/conf/datasources/metrics-datasources.xml"],
                    "product-is":  ["repository/conf/datasources/master-datasources.xml",
                    			"repository/conf/datasources/metrics-datasources.xml",
					 "repository/conf/datasources/bps-datasources.xml"],
                    "product-ei": []}
DIST_POM_PATH = {"product-is": "modules/distribution/pom.xml", "product-apim": "modules/distribution/product/pom.xml",
                 "product-ei": "distribution/pom.xml"}
LIB_PATH = "repository/components/lib"
DISTRIBUTION_PATH = {"product-apim": "modules/distribution/product/target",
                     "product-is": "modules/distribution/target",
                     "product-ei": "modules/distribution/target"}
PRODUCT_STORAGE_DIR_NAME = "storage"
TEST_PLAN_PROPERTY_FILE_NAME = "testplan-props.properties"
INFRA_PROPERTY_FILE_NAME = "infrastructure.properties"
LOG_FILE_NAME = "integration.log"
ORACLE_DB_ENGINE = "ORACLE-SE2"
MSSQL_DB_ENGINE = "SQLSERVER-SE"
MYSQL_DB_ENGINE = "MYSQL"
DEFAULT_ORACLE_SID = "orcl"
DB_CARBON_DB = 'WSO2_CARBON_DB'
#DB_AM_DB = 'WSO2AM_DB'
DB_PRODUCT_DB = {"product-apim": "WSO2AM_DB",
                     "product-is": "WSO2IS_DB",
                     "product-ei": "WSO2EI_DB"}
#DB_IS_DB = 'WSO2IS_DB'
DB_STAT_DB = 'WSO2_STATS_DB'
DB_BPS_DB = 'BPS_DS'
DB_METRICS_DB = 'WSO2_METRICS_DB'
DEFAULT_DB_USERNAME = "wso2carbon"
LOG_STORAGE = "logs"
LOG_FILE_PATHS = {"product-apim": [
    "modules/integration/tests-integration/tests-backend/target/surefire-reports/emailable-report.html",
    "modules/integration/tests-integration/tests-backend/target/surefire-reports/index.html",
    "modules/integration/tests-integration/tests-backend/target/surefire-reports/TEST-TestSuite.xml",
    "modules/integration/tests-integration/tests-backend/target/surefire-reports/testng.css",
    "modules/integration/tests-integration/tests-backend/target/surefire-reports/testng-results.xml",
    "modules/integration/tests-integration/tests-backend/target/surefire-reports/TestSuite.txt",
    "modules/integration/tests-integration/tests-backend/target/logs/automation.log"],
    "product-is": [
	"modules/integration/tests-integration/tests-backend/target/surefire-reports/emailable-report.html",
	"modules/integration/tests-integration/tests-backend/target/surefire-reports/index.html",
	"modules/integration/tests-integration/tests-backend/target/surefire-reports/TEST-TestSuite.xml",
	"modules/integration/tests-integration/tests-backend/target/surefire-reports/testng.css",
	"modules/integration/tests-integration/tests-backend/target/surefire-reports/testng-results.xml",
	"modules/integration/tests-integration/tests-backend/target/surefire-reports/TestSuite.txt",
	"modules/integration/tests-integration/tests-backend/target/logs/automation.log"],
    "product-ei": []}
DB_META_DATA = {
    "MYSQL": {"prefix": "jdbc:mysql://", "driverClassName": "com.mysql.jdbc.Driver", "jarName": "mysql.jar"},
    "SQLSERVER-SE": {"prefix": "jdbc:sqlserver://",
                     "driverClassName": "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jarName": "sqlserver-ex.jar"},
    "ORACLE-SE2": {"prefix": "jdbc:oracle:thin:@", "driverClassName": "oracle.jdbc.OracleDriver",
                   "jarName": "oracle-se.jar"},
    "POSTGRESQL": {"prefix": "jdbc:postgresql://", "driverClassName": "org.postgresql.Driver",
                   "jarName": "postgres.jar"}
}
