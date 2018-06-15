# Scenario 26 - User administration operations from a third-party web app

### SCENARIO DESCRIPTION

##### Problem:

A third party web app needs to perform all user management operations such as all CRUD operations on users and roles, user/role assignments and password recovery, without having to deal directly with underlying user stores (LDAP, AD, JDBC).


##### Scenario:

1. Deploy the WSO2 Identity Server over the required set of user stores.
2. The WSO2 Identity Server exposes a set of REST endpoints as well as SOAP-based services for user management, the web app just need to talk to these endpoints, without having to deal directly with underlying user stores (LDAP, AD, JDBC).

Products: WSO2 Identity Server 4.0.0+


### Run the test
1. Export tomcatHost, tomcatPost, serverHost, serverPort, JMETER_HOME, tomcatUsername, tomcatPassword as below. 

export serverHost=localhost serverPort=9443 JMETER_HOME= <JMETER_HOME>/apache-jmeter-3.3

2. Go to testsuite home and execute below commmand to run the test script. 

>sh run-scenario.sh


