$productHome
filePath=/repository/deployment/server/webapps/authenticationendpoint

prgdir=$(dirname "$0")
configDir=$(cd "$prgdir"; pwd)


########### RESTARTING THE SERVER ONCE ###########

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
#mystatus=$(curl -s -w '%{http_code}' https://localhost:9443/carbon -k )
if curl -s -w '%{http_code}' https://localhost:9443/carbon -k | grep "000"
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
x=$((x+1))
sleep 1
done
#wait few seconds to finish with server-stop
sleep 3
#start back the server
echo "server starting..."
sh wso2server.sh start
#wait till server starts
x=0;
retry_count=20;
while true
do
echo $(date)" waiting until server starts..."
#STATUS=$(curl -s http://scriptuser:scriptuser@localhost:8080/manager/text/list | grep ${appName})
if curl -s -w '%{http_code}' https://localhost:9443/carbon -k | grep "302"
then
 echo "found server running..."
 echo "configurations Done...!"
 break
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

###########

#copy config files
cd $productHome/repository/deployment/server/webapps/
mkdir authenticationendpoint
cd $productHome
cp $configDir/files/pwd-reset.jsp $productHome/$filePath
echo "pwd-reset.jsp file added to the path: $productHome/$filePath"


#build the product
cd $productHome
mkdir passwordpolicy
cd passwordpolicy
git clone https://github.com/wso2-extensions/identity-outbound-auth-passwordPolicy.git
cd identity-outbound-auth-passwordPolicy
mvn clean install
echo "Authenticator jar file is built"

pwd
cp $productHome/passwordpolicy/identity-outbound-auth-passwordPolicy/component/authenticator/target/*.jar $productHome/repository/components/dropins/
echo "Authenticator jar is built and copied to dropins folder"

cd $productHome
rm -rf passwordpolicy/

#update identity-mgt.properties
value="Authentication.Policy.Password.Reset.Time.In.Days=20"
file=identity-mgt.properties
echo $value >> $productHome/repository/conf/identity/$file
echo "Value; $value added to the file: $file"

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
#mystatus=$(curl -s -w '%{http_code}' https://localhost:9443/carbon -k )
if curl -s -w '%{http_code}' https://localhost:9443/carbon -k | grep "000"
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
x=$((x+1))
sleep 1
done
#wait few seconds to finish with server-stop
sleep 3
#start back the server
echo "server starting..."
sh wso2server.sh start
#wait till server starts
x=0;
retry_count=20;
while true
do
echo $(date)" waiting until server starts..."
#STATUS=$(curl -s http://scriptuser:scriptuser@localhost:8080/manager/text/list | grep ${appName})
if curl -s -w '%{http_code}' https://localhost:9443/carbon -k | grep "302"
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
