#!/bin/sh

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

prgdir=$(dirname "$0")
rootPath=$(cd "$prgdir"; pwd)

#JMeter
JmeterVersion=$JmeterVersion
defaultVersion=3.3

##Installing Jmeter
mkdir $rootPath/../Jmeter
cd $rootPath/../Jmeter/

#if Jmeter version is provided then this will download and install the provided version 
# otherwise it will download and install the default version (default for the specific branch) 
if [ -z "$JmeterVersion" ]; then
   echo "JmeterVersion is empty, so proceed with the default jmeter runtime."
   echo "Downloading apache-jmeter-$defaultVersion.zip..."
   curl -O https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-$defaultVersion.zip
   echo "Extracting apache-jmeter-$defaultVersion.zip..."
   unzip apache-jmeter-$defaultVersion.zip
   export JMETER_HOME=$rootPath/../Jmeter/apache-jmeter-$defaultVersion
else
   echo "Downloading apache-jmeter-$JmeterVersion.zip..."
   curl -O https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-$JmeterVersion.zip
   echo "Extracting apache-jmeter-$JmeterVersion.zip..."
   unzip apache-jmeter-$JmeterVersion.zip
   export JMETER_HOME=$rootPath/../Jmeter/apache-jmeter-$JmeterVersion
fi

echo "JMETER_HOME: " $JMETER_HOME
