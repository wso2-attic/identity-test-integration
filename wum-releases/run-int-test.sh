#----------------------------------------------------------------------------
#  Copyright (c) 2020 WSO2, Inc. http://www.wso2.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#----------------------------------------------------------------------------
#!/bin/bash

set -o xtrace

WORKING_DIR=$(pwd)
PRODUCT_REPOSITORY=$1
PRODUCT_REPOSITORY_BRANCH=$2
PRODUCT_NAME=$3
PRODUCT_VERSION=$4
GIT_USER=$5
GIT_PASS=$6

PRODUCT_REPOSITORY_NAME=$(echo $PRODUCT_REPOSITORY | rev | cut -d'/' -f1 | rev | cut -d'.' -f1)
LOCAL_PRODUCT_PACK_LOCATION="/mnt/is"
PRODUCT_REPOSITORY_PACK_DIR="$WORKING_DIR/$PRODUCT_REPOSITORY_NAME/modules/distribution/target"
INT_TEST_MODULE_DIR="$WORKING_DIR/$PRODUCT_REPOSITORY_NAME/modules/integration"
NEXUS_SCRIPT_NAME="uat-nexus-settings.xml"
INFRA_JSON="infra.json"

# CloudFormation properties
CFN_PROP_FILE="${WORKING_DIR}/cfn-props.properties"
JDK_TYPE=$(grep -w "JDK_TYPE" ${CFN_PROP_FILE} | cut -d"=" -f2)
DB_TYPE=$(grep -w "DB_TYPE" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_VERSION=$(grep -w "CF_DB_VERSION" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_PASSWORD=$(grep -w "CF_DB_PASSWORD" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_USERNAME=$(grep -w "CF_DB_USERNAME" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_HOST=$(grep -w "CF_DB_HOST" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_PORT=$(grep -w "CF_DB_PORT" ${CFN_PROP_FILE} | cut -d"=" -f2)
CF_DB_NAME=$(grep -w "SID" ${CFN_PROP_FILE} | cut -d"=" -f2)

function log_info(){
    echo "[INFO][$(date '+%Y-%m-%d %H:%M:%S')]: $1"
}

function install_jdk(){
    jdk_name=$1

    mkdir -p /opt/${jdk_name}
    jdk_file=$(jq -r '.jdk[] | select ( .name == '\"${jdk_name}\"') | .file_name' ${INFRA_JSON})
    wget -q https://integration-testgrid-resources.s3.amazonaws.com/lib/jdk/$jdk_file.tar.gz
    tar -xzf "$jdk_file.tar.gz" -C /opt/${jdk_name} --strip-component=1

    export JAVA_HOME=/opt/${jdk_name}
    echo $JAVA_HOME
}

echo "Test script running"

log_info "Clone Product repository"
git clone https://${GIT_USER}:${GIT_PASS}@$PRODUCT_REPOSITORY --branch $PRODUCT_REPOSITORY_BRANCH --single-branch

mkdir -p $PRODUCT_REPOSITORY_PACK_DIR

log_info "Copying product pack to Repository"
cd $LOCAL_PRODUCT_PACK_LOCATION && zip -qr $PRODUCT_NAME-$PRODUCT_VERSION.zip $PRODUCT_NAME-$PRODUCT_VERSION
cp $LOCAL_PRODUCT_PACK_LOCATION/$PRODUCT_NAME-$PRODUCT_VERSION.zip $PRODUCT_REPOSITORY_PACK_DIR/$PRODUCT_NAME-$PRODUCT_VERSION.zip
cd ${WORKING_DIR}
mv $WORKING_DIR/$NEXUS_SCRIPT_NAME $INT_TEST_MODULE_DIR/.

install_jdk $JDK_TYPE

cd $INT_TEST_MODULE_DIR  && mvn clean install -U -s $NEXUS_SCRIPT_NAME -fae -B -Dorg.slf4j.simpleLogger.log.org.apache.maven.cli.transfer.Slf4jMavenTransferListener=warn
