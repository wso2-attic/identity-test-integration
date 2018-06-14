#!/bin/bash
# Copyright (c) 2017, WSO2 Inc. (http://wso2.com) All Rights Reserved.
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


#properties
#TODO:read below property from infra.json file
appName="Sol17amazon"
tomcatHost=$tomcatHost
tomcatPort=$tomcatPort
tomcatUsername=$tomcatUsername
tomcatPassword=$tomcatPassword
tomcatVersion=7
serverHost=$serverHost
serverPort=$serverPort
solutionPath=/


#create temporary directory
mkdir $scriptPath ./temp

#coping Sol17amazon app to temp direcory

cp -r ../apps/Sol17amazon/ temp/

cd temp/Sol17amazon
mvn clean install
pwd
#move the Sol17amazon.war file inside the temp folder
mv target/Sol17amazon.war  ../


##############################################
#move out to the temp folder 
cd ..

#deploy webapp on tomcat
pwd
#tomcat6
#curl --upload-file target\debug.war "http://tomcat:tomcat@localhost:8088/manager/deploy?path=/debug&update=true"
#tomcat7/8
#curl -T "Sol17amazon.war" "http://$tomcatUsername:$tomcatPassword@$tomcatHost:$tomcatPort/manager/text/deploy?path=Sol17amazon&update=true"
curl -T "Sol17amazon.war" "http://$tomcatUsername:$tomcatPassword@$tomcatHost:$tomcatPort/manager/text/deploy?path=${solutionPath}${appName}&update=true"
x=0;
retry_count=10;
while true
do
echo $(date)" Waiting until deploying the app on Tomcat!"
#STATUS=$(curl -s http://$scriptuser:$scriptuser@localhost:8080/manager/text/list | grep ${appName})
if curl -s http://$tomcatUsername:$tomcatPassword@$tomcatHost:$tomcatPort/manager/text/list | grep "${appName}:running"
then
 echo "Found ${appName} is running on Tomcat"
 echo "Done base-setup.sh"
 exit 0
else
 echo "Context /${appName} Not Found"
    if [ $x = $retry_count ]; then
    echo "ERROR on app deployment"
        exit 1
    fi
fi
x=$((x+1))
sleep 1
done
