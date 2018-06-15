#include the path of the IS Pack for the productHome variable when trying locally
#################################################
#Examples
#productHome=/home/shavantha/products/wso2is/550/wso2is-5.5.0
#configSetHome=/home/shavantha/products/jmeter/apache-jmeter-3.3/bin/isscripts/shavantha/identity-test-integration/config-sets/config04
##################################################

productHome=/home/shavantha/products/wso2is/550/wso2is-5.5.0
configSetHome=/home/shavantha/products/jmeter/apache-jmeter-3.3/bin/isscripts/shavantha/identity-test-integration/config-sets/config05

libPath=repository/components/lib/
dropinsPath=repository/components/dropins/
mysqlJAR=mysql-connector-java-5.1.42-bin.jar

serverHost=$serverHost
serverPort=$serverPort



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


cp $configSetHome/jars/$mysqlJAR $productHome/$libPath

cp $configSetHome/jars/org.soasecurity.user.mgt.attribute.store.extension-1.0.0.jar $productHome/$dropinsPath


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
