#!/bin/bash
rm -rf ./apache-tomcat-7.0.68
tar xzvf apache-tomcat-7.0.68.tar.gz
cp ./travelocity.com.war ./apache-tomcat-7.0.68/webapps/
sh ./apache-tomcat-7.0.68/bin/startup.sh
