#!/bin/sh

# Copyright (c) 2018, WSO2 Inc. (http://wso2.com) All Rights Reserved.
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

#use sudo su command and hit enter to give root permissions
#run the file with the command sh init.sh 


# PATH TO YOUR HOSTS FILE
ETC_HOSTS=/etc/hosts

# IP Name and IP Adress 
# IP Address need to be set to a variable sent from the testgrid side including the IP Address of the Load balancer
IPName="is.qa.com"
IPLoadBalancer=$serverHost

if [ -z "$IPLoadBalancer" ]; then
   echo "IPLoadBalancer is empty, please initiate it and proceed."
   exit 1;
else
if [ -n "$(grep $IPName $ETC_HOSTS)" ]; then
	echo "$IPName already exists : $(grep $IPName $ETC_HOSTS)"
else
    PublicIP="$(ping -c 1 $IPLoadBalancer | grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')"
    HOSTS_LINE="$PublicIP\t$IPName"
	echo "Adding $IPName to your $ETC_HOSTS";
   	sudo -- sh -c -e "echo '$HOSTS_LINE' >> $ETC_HOSTS";
   	if [ -n "$(grep $IPName $ETC_HOSTS)" ]; then
       		echo "$IPName was added succesfully \n $(grep $IPName $ETC_HOSTS)";
    	else
       		echo "Failed to Add $IPName, Try again!";
    	fi
fi
fi
