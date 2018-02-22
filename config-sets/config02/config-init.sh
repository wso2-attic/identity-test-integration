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
#run the file with the command sh config-init.sh


#xml starlet will be installed with the Y option selected through the shell script for the question Do you want to continue?

if dpkg -l | grep "xmlstarlet"; then
	echo "xmlstarlet exists!"
  	exit 0
else
	echo "Module is Installing"
	sudo apt-get -y install xmlstarlet
fi
if dpkg -l | grep "xmlstarlet"; then
	echo "Successfully installed"
  	exit 0
else
	echo "installation failed"
	exit 1
fi
