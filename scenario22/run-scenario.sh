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

prgdir=$(dirname "$0")
scriptPath=$(cd "$prgdir"; pwd)


sh $scriptPath/jmeter/22-pre-scenario-steps.sh

$JMETER_HOME/bin/jmeter.sh -n -t jmeter/01-Scenario-22-Create-Test-Users.jmx -p resources/user.properties
$JMETER_HOME/bin/jmeter.sh -n -t jmeter/02-Scenario-22-Create-IDP.jmx -p resources/user.properties
$JMETER_HOME/bin/jmeter.sh -n -t jmeter/03-Scenario-22-Create-SP.jmx -p resources/user.properties
$JMETER_HOME/bin/jmeter.sh -n -t jmeter/04-Scenario-22-SAML2-Get-JWT-Token -p resources/user.properties
$JMETER_HOME/bin/jmeter.sh -n -t jmeter/05-Scenario-22-Delete-IDP.jmx -p resources/user.properties
$JMETER_HOME/bin/jmeter.sh -n -t jmeter/06-Scenario-22-Delete-SP.jmx -p resources/user.properties
$JMETER_HOME/bin/jmeter.sh -n -t jmeter/07-Scenario-22-Remove-Test-Users.jmx -p resources/user.properties

sh $scriptPath/jmeter/22-post-scenario-steps.sh
