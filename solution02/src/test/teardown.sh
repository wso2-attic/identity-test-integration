#these params need to be taken out
#tomcat properties
tomcat_host="ec2-54-152-226-196.compute-1.amazonaws.com"
tomcat_port=8080
tomcat_username=scriptuser
tomcat_password=scriptuser
app_name="travelocity.com"

#undeploy webapp from tomcat
curl http://$tomcat_username:$tomcat_password@$tomcat_host:$tomcat_port/manager/text/undeploy?path=/$app_name
#clear temp direcotry
rm -rf $script_path/../temp/
