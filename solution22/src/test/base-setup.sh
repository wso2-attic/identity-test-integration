#!/bin/bash
#properties
#TODO:read below property from infra.json file
appName="travelocity.com"
tomcatHost=$tomcatHost
tomcatPort=8080
tomcatUsername=scriptuser
tomcatPassword=scriptuser
tomcatVersion=7
serverHost=$serverHost
serverPort=443
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
#TODO:need to get the actual response from above command and set blow..
#TODO:check if any error occured
echo "Done..."
