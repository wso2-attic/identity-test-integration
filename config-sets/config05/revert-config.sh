#include the path of the IS Pack for the productHome variable when trying locally
productHome=/home/shavantha/products/wso2is/550/wso2is-5.5.0
configSetHome=/home/shavantha/products/jmeter/apache-jmeter-3.3/bin/isscripts/shavantha/identity-test-integration/config-sets/config05

libPath=repository/components/lib/
dropinsPath=repository/components/dropins/

mysqlJAR=mysql-connector-java-5.1.42-bin.jar

serverHost=$serverHost
serverPort=$serverPort

file=$productHome/repository/conf/identity/identity.xml

xmlstarlet edit -L -N w=http://wso2.org/projects/carbon/carbon.xml \
-u "/w:Server/w:OAuth/w:OpenIDConnect \
/w:SkipUserConsent" -v "false" $file

if [ $? -ne 0 ]; then
    echo "Could not find the file in the given location"
    exit 1
fi

echo "Values added to the file: $file"

cd $productHome/bin

#verify file copy status and exit on failure
statusval=$?
if [ $statusval -eq 0 ]; then
 echo "file copying success!"
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
sleep 10

echo "removing the conf file"
cd $productHome/$libPath

#Remove the mysql jar

rm $mysqlJAR 
echo "file deleted"

cd $productHome/$dropinsPath
rm org.soasecurity.user.mgt.attribute.store.extension-1.0.0.jar 

cd $productHome/bin

#start back the server
echo "server starting..."
sh wso2server.sh start
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
