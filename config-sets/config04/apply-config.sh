#include the path of the IS Pack for the productHome variable when trying locally
#################################################
#Examples
#productHome=/home/shavantha/products/wso2is/550/wso2is-5.5.0
#configSetHome=/home/shavantha/products/jmeter/apache-jmeter-3.3/bin/isscripts/shavantha/identity-test-integration/config-sets/config04
##################################################

productHome=$productHome
configSetHome="$( cd "$(dirname "$0")" ; pwd -P )"
folderPath=/repository/conf/
webappPath=/repository/deployment/server/webapps/


if [ -z "$serverHost" ]; then
    serverHost=localhost
else
    serverHost=$serverHost
fi
if [ -z "$serverPort" ]; then
    serverPort=9443
else
    serverPort=$serverPort
fi

TomcatServerHost=$tomcatHost
TomcatServerPort=$tomcatPort



cd $productHome/bin

#verify file copy status and exit on failure
statusval=$?
if [ $statusval -eq 0 ]; then
 echo "Configuration change is successful!"
 #stop the server
 echo "shutting down the server now..."
 sh wso2server.sh stop
else
    echo "file copy command failed..."
    exit 1
fi
#wait till server stops
y=0;
retry_count1=20;
while true
do
echo $(date)" Waiting until server stops"
if curl -s -w '%{http_code}' https://$serverHost:$serverPort/carbon -k | grep "000"
then
 echo "Carbon server stopped...!"
 break
else
 echo "Carbon server is still running..."
    if [ $y = $retry_count1 ]; then
    echo "Couldn't stop the server"
        exit 1
    fi
fi
y=$((y+1))
sleep 1
done
#wait few seconds to finish with server-stop
sleep 5
echo "getting ready to add the file"


echo "====================================================="
echo "copying the file........."
cd $productHome/$folderPath
touch oauth_proxy.properties

 echo "is_server_ep=https://"${serverHost}:${serverPort} >> oauth_proxy.properties

 echo "client_id=6ktdbCJgmQIqlO1tNiHBQoVelkUlg" >> oauth_proxy.properties

 echo "client_secret=cg5Gg8PfwI28NjLRy64pyffcK4Ilg" >> oauth_proxy.properties

 echo "proxy_callback_url=https://"${serverHost}:${serverPort}"/oauth2-proxy/callback" >> oauth_proxy.properties

 echo "sp_callback_url_mapping.sample1=http://"${TomcatServerHost}:${TomcatServerPort}"/Sol17amazon/in.html" >> oauth_proxy.properties

 echo "sp_logout_url_mapping.sample1=http://"${TomcatServerHost}:${TomcatServerPort}"/Sol17amazon/index.html" >> oauth_proxy.properties

 echo "iv=RandomInitVector" >> oauth_proxy.properties

 echo "secret_key=Bar12345Bar12345" >> oauth_proxy.properties

echo "finished creating the file"
echo "====================================================="
sleep 5

#Move to the config set home and copy the oauth2-proxy.war to webapps of the identity server
cd $configSetHome
cp oauth2-proxy.war $productHome/$webappPath


file=$productHome/repository/conf/identity/identity.xml

xmlstarlet edit -L -N w=http://wso2.org/projects/carbon/carbon.xml \
-u "/w:Server/w:OAuth/w:OpenIDConnect \
/w:SkipUserConsent" -v "true" $file

if [ $? -ne 0 ]; then
    echo "Could not find the file in the given location"
    exit 1
fi

echo "Values added to the file: $file"


cd $productHome/bin

#start back the server
echo "server starting..."
sh wso2server.sh start

echo "---------------------"
#wait till server starts
x=0;
retry_count=20;
while true
do
echo $(date)" waiting until server starts..."
if curl -s -w '%{http_code}' https://$serverHost:$serverPort/carbon -k | grep "302"
then
 echo "found server running..."
 echo "configurations Done...!"
 exit 0
else
 echo "carbon server not running..."
    if [ $x = $retry_count ]; then
    echo "Couldn't start the server"
        exit 1
    fi
fi
x=$((x+1))
sleep 3
done
