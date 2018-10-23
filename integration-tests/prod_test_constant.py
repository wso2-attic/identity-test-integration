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
DATASOURCE_PATHS = {"repository/conf/datasources/master-datasources.xml",
                    "repository/conf/datasources/metrics-datasources.xml",
                    "repository/conf/datasources/bps-datasources.xml"}
M2_PATH = "is/wso2is"
DIST_POM_PATH = "modules/distribution/pom.xml"
LIB_PATH = "repository/components/lib"
DISTRIBUTION_PATH = "modules/distribution/target"
INTEGRATION_PATH = "modules/integration/tests-integration/tests-backend"
POM_FILE_PATHS = {}
TESTNG_DIST_XML_PATHS = {}
TESTNG_SERVER_MGT_DIST = {}
ARTIFACT_REPORTS_PATHS = {"modules/integration/tests-integration/tests-backend/target/logs/automation.log",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/emailable-report.html",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/index.html",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/TEST-TestSuite.xml",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/testng.css",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/testng-results.xml",
        "modules/integration/tests-integration/tests-backend/target/surefire-reports/TestSuite.txt"}
DB_META_DATA = {
    "MYSQL": {"prefix": "jdbc:mysql://", "driverClassName": "com.mysql.jdbc.Driver", "jarName": "mysql.jar",
              "DB_SETUP": {"WSO2_CARBON_DB": ['dbscripts/mysql5.7.sql',
                                              'dbscripts/identity/mysql-5.7.sql'],
                           "WSO2_METRICS_DB": ['dbscripts/metrics/mysql.sql'],
                           "BPS_DS": ['dbscripts/bps/bpel/create/mysql.sql']}
              },

    "SQLSERVER-SE": {"prefix": "jdbc:sqlserver://",
                     "driverClassName": "com.microsoft.sqlserver.jdbc.SQLServerDriver", "jarName": "sqlserver-ex.jar",
                     "DB_SETUP": {"WSO2_CARBON_DB": ['dbscripts/mssql.sql',
                                                     'dbscripts/identity/mssql.sql'],
                                  "WSO2_METRICS_DB": ['dbscripts/metrics/mssql.sql'],
                                  "BPS_DS": ['dbscripts/bps/bpel/create/mssql.sql']}
                     },

    "ORACLE-SE2": {"prefix": "jdbc:oracle:thin:@", "driverClassName": "oracle.jdbc.OracleDriver",
                   "jarName": "oracle-se.jar",
                   "DB_SETUP": {"WSO2_CARBON_DB": ['dbscripts/oracle.sql',
                                                   'dbscripts/identity/oracle.sql'],
                                "WSO2_METRICS_DB": ['dbscripts/metrics/oracle.sql'],
                                "BPS_DS": ['dbscripts/bps/bpel/create/oracle.sql']}
                   },

    "POSTGRESQL": {"prefix": "jdbc:postgresql://", "driverClassName": "org.postgresql.Driver",
                   "jarName": "postgres.jar",
                   "DB_SETUP": {"WSO2_CARBON_DB": ['dbscripts/postgresql.sql',
                                                   'dbscripts/identity/postgresql.sql'],
                                "WSO2_METRICS_DB": ['dbscripts/metrics/postgresql.sql'],
                                "BPS_DS": ['dbscripts/bps/bpel/create/postgresql.sql']}
                   }
}
