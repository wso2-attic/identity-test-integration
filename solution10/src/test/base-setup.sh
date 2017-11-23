#!/bin/bash
#properties
#TODO:read below property from infra.json file
app_name="travelocity.com"
tomcat_host=$tomcat_host
tomcat_port=8080
tomcat_username=scriptuser
tomcat_password=scriptuser
tomcat_version=7
server_host=$server_host
server_port=443
solution_path=/

#travelocity properties
SAML2AssertionConsumerURL="http://$tomcat_host:$tomcat_port/$app_name/home.jsp"
SAML2IdPURL="https://$server_host/samlsso"
SAML2SPEntityId="$app_name"
SkipURIs="/$app_name/index.jsp"
SAML2IdPEntityId="$server_host"
OAuth2TokenURL="https://$server_host:$server_port/oauth2/token"
OAuth2ClientId="lKjE0YDVrXNJY8TN7AdzAgkgfJ0a"
OAuth2ClientSecret="KiAnWzcf9NaKCdL7B8wjGqffE70a"
OpenIdProviderURL="https://$server_host:$server_port/openid/"
OpenIdReturnToURL="http://$tomcat_host:$tomcat_port/travelocity.com/home.jsp"

#create temporary directory
mkdir $script_path/../temp
#coping travalocity app to temp direcory
cp -r $script_path/../../../../apps/travelocity.com/ $script_path/../temp

#updating travelocity.conf file
sed -i "s|^\(SAML2\.AssertionConsumerURL\s*=\s*\).*\$|\1${SAML2AssertionConsumerURL}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.IdPURL\s*=\s*\).*\$|\1${SAML2IdPURL}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.SPEntityId\s*=\s*\).*\$|\1${SAML2SPEntityId}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SkipURIs\s*=\s*\).*\$|\1${SkipURIs}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(SAML2\.IdPEntityId\s*=\s*\).*\$|\1${SAML2IdPEntityId}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(OAuth2\.TokenURL\s*=\s*\).*\$|\1${OAuth2TokenURL}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(OAuth2\.ClientId\s*=\s*\).*\$|\1${OAuth2ClientId}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(OAuth2\.ClientSecret\s*=\s*\).*\$|\1${OAuth2ClientSecret}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(OpenId\.ProviderURL\s*=\s*\).*\$|\1${OpenIdProviderURL}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

sed -i "s|^\(OpenId\.ReturnToURL\s*=\s*\).*\$|\1${OpenIdReturnToURL}|" $script_path/../temp/travelocity.com/WEB-INF/classes/travelocity.properties

#repackaging travelocity app
cd $script_path/../temp/travelocity.com/
jar cvf $script_path/../temp/travelocity.com.war .

#deploy webapp on tomcat
cd $script_path/../temp/
#tomcat6
#curl --upload-file target\debug.war "http://tomcat:tomcat@localhost:8088/manager/deploy?path=/debug&update=true"
#tomcat7/8
curl -T "travelocity.com.war" "http://$tomcat_username:$tomcat_password@$tomcat_host:$tomcat_port/manager/text/deploy?path=/travelocity.com&update=true"
#TODO:need to get the actual response from above command and set blow..
#TODO:check if any error occured
echo "Done..."
