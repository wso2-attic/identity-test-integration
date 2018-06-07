#! /bin/bash

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

appName1="travelocity.com"
appName2="avis.com"
tomcatHost=$tomcatHost
tomcatPort=$tomcatPort
tomcatUsername=$tomcatUsername
tomcatPassword=$tomcatPassword
tomcatVersion=7
serverHost=$serverHost
serverPort=$serverPort
solutionPath=/

#web app properties
SAML2AssertionConsumerURL1="http://$tomcatHost:$tomcatPort/$appName1/home.jsp"
SAML2AssertionConsumerURL2="http://$tomcatHost:$tomcatPort/$appName2/home.jsp"
SAML2IdPURL="https://$serverHost:$serverPort/samlsso"
SAML2SPEntityId1="$appName1"
SAML2SPEntityId2="$appName2"
SkipURIs1="/$appName1/index.jsp"
SkipURIs2="/$appName2/index.jsp"
SAML2IdPEntityId=$serverHost
EnableResponseSigning="false"
EnableAssertionSigning="false"
EnableRequestSigning="false"


#create temporary directory
mkdir $scriptPath/../temp

#copying sso sample app to temp direcory

cp -r $scriptPath/../../apps/sso-agent-sample $scriptPath/../temp/
cd $scriptPath/../temp/sso-agent-sample/

#build travelocity and avis app from source
mvn clean install
mkdir $scriptPath/../temp/travelocity.com
mkdir $scriptPath/../temp/avis.com

cd $scriptPath/../temp/sso-agent-sample/target
cp -r travelocity.com.war avis.com.war

#extract travelocity.com.war to temp directory for further configurations
cd $scriptPath/../temp/travelocity.com
jar xvf $scriptPath/../temp/sso-agent-sample/target/travelocity.com.war

#updating travelocity.conf file
sed -i "s|^\(SAML2\.AssertionConsumerURL\s*=\s*\).*\$|\1${SAML2AssertionConsumerURL1}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.IdPURL\s*=\s*\).*\$|\1${SAML2IdPURL}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.SPEntityId\s*=\s*\).*\$|\1${SAML2SPEntityId1}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SkipURIs\s*=\s*\).*\$|\1${SkipURIs1}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.IdPEntityId\s*=\s*\).*\$|\1${SAML2IdPEntityId}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.EnableResponseSigning\s*=\s*\).*\$|\1${EnableResponseSigning}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.EnableAssertionSigning\s*=\s*\).*\$|\1${EnableAssertionSigning}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.EnableRequestSigning\s*=\s*\).*\$|\1${EnableRequestSigning}|" $scriptPath/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

#repackaging travelocity app
cd $scriptPath/../temp/travelocity.com/
jar cvf $scriptPath/../temp/travelocity.com.war .

#extract avis.com.war to temp directory for further configurations
cd $scriptPath/../temp/avis.com
jar xvf $scriptPath/../temp/sso-agent-sample/target/avis.com.war

#updating avis.conf file
sed -i "s|^\(SAML2\.AssertionConsumerURL\s*=\s*\).*\$|\1${SAML2AssertionConsumerURL2}|" $scriptPath/../temp/avis.com/WEB-INF/classes/avis.properties

sed -i "s|^\(SAML2\.IdPURL\s*=\s*\).*\$|\1${SAML2IdPURL}|" $scriptPath/../temp/avis.com/WEB-INF/classes/avis.properties

sed -i "s|^\(SAML2\.SPEntityId\s*=\s*\).*\$|\1${SAML2SPEntityId2}|" $scriptPath/../temp/avis.com/WEB-INF/classes/avis.properties

sed -i "s|^\(SkipURIs\s*=\s*\).*\$|\1${SkipURIs2}|" $scriptPath/../temp/avis.com/WEB-INF/classes/avis.properties

sed -i "s|^\(SAML2\.IdPEntityId\s*=\s*\).*\$|\1${SAML2IdPEntityId}|" $scriptPath/../temp/avis.com/WEB-INF/classes/avis.properties

sed -i "s|^\(SAML2\.EnableResponseSigning\s*=\s*\).*\$|\1${EnableResponseSigning}|" $scriptPath/../temp/avis.com/WEB-INF/classes/avis.properties

sed -i "s|^\(SAML2\.EnableAssertionSigning\s*=\s*\).*\$|\1${EnableAssertionSigning}|" $scriptPath/../temp/avis.com/WEB-INF/classes/avis.properties

sed -i "s|^\(SAML2\.EnableRequestSigning\s*=\s*\).*\$|\1${EnableRequestSigning}|" $scriptPath/../temp/avis.com/WEB-INF/classes/avis.properties

#repackaging avis app
cd $scriptPath/../temp/avis.com/
jar cvf $scriptPath/../temp/avis.com.war .


#deploy webapp on tomcat
cd $scriptPath/../temp/
#tomcat6
#curl --upload-file target\debug.war "http://tomcat:tomcat@localhost:8088/manager/deploy?path=/debug&update=true"
#tomcat7/8
curl -T "travelocity.com.war" "http://$tomcatUsername:$tomcatPassword@$tomcatHost:$tomcatPort/manager/text/deploy?path=/travelocity.com&update=true"
curl -T "avis.com.war" "http://$tomcatUsername:$tomcatPassword@$tomcatHost:$tomcatPort/manager/text/deploy?path=/avis.com&update=true"


x=0;
retry_count=10;
while true
do
echo $(date)" Waiting until deploying the app on Tomcat!"
#STATUS=$(curl -s http://$scriptuser:$scriptuser@localhost:8080/manager/text/list | grep ${appName})
if curl -s http://$tomcatUsername:$tomcatPassword@$tomcatHost:$tomcatPort/manager/text/list | grep "${appName1}:running" &&
	curl -s http://$tomcatUsername:$tomcatPassword@$tomcatHost:$tomcatPort/manager/text/list | grep "${appName2}:running"
then
 echo "Found ${appName1} is running on Tomcat"
 echo "Found ${appName2} is running on Tomcat"

 echo "Done base-setup.sh"
 exit 0
else
 echo "Context /${appName2} Not Found"
    if [ $x = $retry_count ]; then
    echo "ERROR on app deployment"
        exit 1
    fi
fi
x=$((x+1))
sleep 1
done
