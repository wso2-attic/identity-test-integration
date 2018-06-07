# Scenario 18 - Fine-grained access control for service providers

### SCENARIO DESCRIPTION

##### Problem:

-The business users need to access multiple service providers supporting multiple heterogeneous identity federation protocols.

-Each service provider needs to define an authorization policy at the identity provider, to decide whether a given user is eligible to log into the corresponding service provider.

-For example, one service provider may have a requirement that only the admin users will be able to login into the system after 6 PM.

-Another service provider may have a requirement that only the users from North America should be able to login into the system.

##### Scenario:

-Deploy WSO2 Identity Server as the Identity Provider and register all the service providers.

-Build a connector, which connects to the WSO2 Identity Server’s XACML engine to perform authorization.

-For each service provider, that needs to enforce access control during the login flow, engage the XACML connector to the 2nd authentication step, under the Local and Outbound Authentication configuration.

-Each service provider, that needs to enforce access control during the login flow, creates its own XACML policies in the WSO2 Identity Server PAP (Policy Administration Point).

-To optimize the XACML policy evaluation, follow a convention to define a target element under each XACML policy, that can uniquely identify the corresponding service provider.

Products: WSO2 Identity Server 5.0.0+


### Configurations
In order to run the test script, do the following steps. 

1. Export tomcatHost, tomcatPost, serverHost, serverPort, JMETER_HOME, tomcatUsername, tomcatPassword as below. 
export serverHost=localhost serverPort=9443 tomcatHost=localhost tomcatPort=8080 JMETER_HOME= <JMETER_HOME>/apache-jmeter-3.3 tomcatUsername=<tomcatUsername> tomcatPassword=<tomcatPassword>

2. Go to testsuite home and execute below commmand to run the test script. 
sh run-scenario.sh

