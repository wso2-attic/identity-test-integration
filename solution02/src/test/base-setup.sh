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
appName="travelocity.com"
tomcatHost=$tomcatHost
tomcatPort=$tomcatPort
tomcatUsername=scriptuser
tomcatPassword=scriptuser
tomcatVersion=7
serverHost=$serverHost
serverPort=$serverPort
solutionPath=/

#travelocity properties
SAML2AssertionConsumerURL="http://$tomcatHost:$tomcatPort/$appName/home.jsp"
SAML2IdPURL="https://$serverHost/samlsso"
SAML2SPEntityId="$appName"
SkipURIs="/$appName/index.jsp"
SAML2IdPEntityId=$serverHost

#create temporary directory
mkdir $scriptPath/../temp
#coping travalocity app to temp direcory

cp -r $scriptPath/../../../../apps/sso-agent-sample $scriptPath/../temp/
cd $scriptPath/../temp/sso-agent-sample/
#build travelocity app from source
mvn clean install
mkdir $scriptPath/../temp/travelocity.com
cd $scriptPath/../temp/travelocity.com
#extract travelocity.com.war to temp directory for further configurations
jar xvf $scriptPath/../temp/sso-agent-sample/target/travelocity.com.war

#updating travelocity.conf file
sed -i "s|^\(SAML2\.AssertionConsumerURL\s*=\s*\).*\$|\1${SAML2AssertionConsumerURL}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.IdPURL\s*=\s*\).*\$|\1${SAML2IdPURL}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.SPEntityId\s*=\s*\).*\$|\1${SAML2SPEntityId}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SkipURIs\s*=\s*\).*\$|\1${SkipURIs}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.IdPEntityId\s*=\s*\).*\$|\1${SAML2IdPEntityId}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

#repackaging travelocity app
cd $scriptPath/../temp/travelocity.com/
jar cvf $scriptPath/../temp/travelocity.com.war .

#deploy webapp on tomcat
cd $scriptPath/../temp/
#tomcat6
#curl --upload-file target\debug.war "http://tomcat:tomcat@localhost:8088/manager/deploy?path=/debug&update=true"
#tomcat7/8
curl -T "travelocity.com.war" "http://$tomcatUsername:$tomcatPassword@$tomcatHost:$tomcatPort/manager/text/deploy?path=/travelocity.com&update=true"

x=0;
retry_count=10;
while true
do
echo $(date)" Waiting until deploying the app on Tomcat!"
#STATUS=$(curl -s http://scriptuser:scriptuser@localhost:8080/manager/text/list | grep ${appName})
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