#!/bin/bash
#properties
#TODO:read below property from infra.json file
appName1="travelocity.com"
appName2="avis.com"
tomcatHost=$tomcatHost
tomcatPort=8080
tomcatUsername=scriptuser
tomcatPassword=scriptuser
tomcatVersion=7
serverHost=$serverHost
serverPort=443
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

#create temporary directory
mkdir $scriptPath/../temp

#coping sso sample app to temp direcory

cp -r $scriptPath/../../../../apps/sso-agent-sample $scriptPath/../temp/
cd $scriptPath/../temp/sso-agent-sample/

#build travelocity app from source
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
#STATUS=$(curl -s http://scriptuser:scriptuser@localhost:8080/manager/text/list | grep ${appName})
if curl -s http://$tomcatUsername:$tomcatPassword@$tomcatHost:$tomcatPort/manager/text/list | grep "${appName2}:running"
then
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
