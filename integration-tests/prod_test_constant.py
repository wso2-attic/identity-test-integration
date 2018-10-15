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

WSO2SERVER = "bin/wso2server"
DATASOURCE_PATHS = {"product-apim": [],
                    "product-is":  ["repository/conf/datasources/master-datasources.xml",
                                    "repository/conf/datasources/metrics-datasources.xml",
                                    "repository/conf/datasources/bps-datasources.xml"],
                    "product-ei": []}
M2_PATH = {"product-is": "is/wso2is",
           "product-apim": "am/wso2am",
           "product-ei": "ei/wso2ei"}
DIST_POM_PATH = {"product-is": "modules/distribution/pom.xml", "product-apim": "modules/distribution/product/pom.xml",
                 "product-ei": "distribution/pom.xml"}
LIB_PATH = "repository/components/lib"
DISTRIBUTION_PATH = {"product-apim": "modules/distribution/product/target",
                     "product-is": "modules/distribution/target",
                     "product-ei": "modules/distribution/target"}
INTEGRATION_PATH = {"product-apim": "modules/integration",
                    "product-is": "modules/integration/tests-integration/tests-backend",
                    "product-ei": "integration"}
POM_FILE_PATHS = {"product-is": "",
                  "product-apim": "",
                  "product-ei": ""}
DB_PRODUCT_DB = {"product-apim": "WSO2AM_DB",
                 "product-is": "WSO2IS_DB",
                 "product-ei": "WSO2EI_DB"}
ARTIFACT_REPORTS_PATHS = {
    "product-apim": [],
    "product-is": ["modules/integration/tests-integration/tests-backend/target/logs/automation.log",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/emailable-report.html",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/index.html",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/TEST-TestSuite.xml",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/testng.css",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/testng-results.xml",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/TestSuite.txt"],
    "product-ei": []}
DB_META_DATA = {
    "MYSQL": {"prefix": "jdbc:mysql://", "driverClassName": "com.mysql.jdbc.Driver", "jarName": "mysql.jar",
              "DB_SETUP": {
                  "product-apim": {},
                  "product-is": {"WSO2_CARBON_DB": ['dbscripts/mysql5.7.sql'],
                                 "WSO2_METRICS_DB": ['dbscripts/metrics/mysql.sql'],
                                 "BPS_DS": ['dbscripts/bps/bpel/create/mysql.sql']},
                  "product-ei": {}
              }},

    "SQLSERVER-SE": {"prefix": "jdbc:sqlserver://",
                     "driverClassName": "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jarName": "sqlserver-ex.jar",
                     "DB_SETUP": {
                         "product-apim": {},
                         "product-is": {
                             "WSO2_CARBON_DB": ['dbscripts/mssql.sql'],
                             "WSO2_METRICS_DB": ['dbscripts/metrics/mssql.sql'],
                             "BPS_DS": ['dbscripts/bps/bpel/create/mssql.sql']
                         },
                         "product-ei": {}
                     }},

    "ORACLE-SE2": {"prefix": "jdbc:oracle:thin:@", "driverClassName": "oracle.jdbc.OracleDriver",
                   "jarName": "oracle-se.jar",
                   "DB_SETUP": {
                       "product-apim": {},
                       "product-is": {
                           "WSO2_CARBON_DB": ['dbscripts/oracle.sql'],
                           "WSO2_METRICS_DB": ['dbscripts/metrics/oracle.sql'],
                           "BPS_DS": ['dbscripts/bps/bpel/create/oracle.sql']
                       },
                       "product-ei": {}
                   }},

    "POSTGRESQL": {"prefix": "jdbc:postgresql://", "driverClassName": "org.postgresql.Driver",
                   "jarName": "postgres.jar",
                   "DB_SETUP": {"product-apim": {},
                                "product-is": {
                                    "WSO2_CARBON_DB": ['dbscripts/postgresql.sql'],
                                    "WSO2_METRICS_DB": ['dbscripts/metrics/postgresql.sql'],
                                    "BPS_DS": ['dbscripts/bps/bpel/create/postgresql.sql']
                                },
                                "product-ei": {}
                                }
                   }
}