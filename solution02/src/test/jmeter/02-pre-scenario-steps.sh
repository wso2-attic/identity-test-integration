#!/bin/bash

# Copyright (c) 2017, WSO2 Inc. (http://wso2.com) All Rights Reserved.
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

server_host=$server_host
prgdir=$(dirname "$0")
script_path=$(cd "$prgdir"; pwd)

#run base-setup.sh to deploy artifacts
source $script_path/../base-setup.sh > $script_path/basesetup.log

echo "working directory : "$script_path
#updating jmeter properties - user.properties
sed -i "s|^\(server_host\s*=\s*\).*\$|\1${server_host}|" $script_path/../resources/user.properties
sed -i "s|^\(server_port\s*=\s*\).*\$|\1${server_port}|" $script_path/../resources/user.properties
sed -i "s|^\(tomcat_host\s*=\s*\).*\$|\1${tomcat_host}|" $script_path/../resources/user.properties
sed -i "s|^\(tomcat_port\s*=\s*\).*\$|\1${tomcat_port}|" $script_path/../resources/user.properties

echo "pre-steps are done..."
