# Scenario 27 - Authenticate the users against one user store but fetch user attributes from multiple other sources

### Problem
The scenario tries to solve the below problem.
  - User credentials are maintained in a one user store while user attributes are maintained in multiple sources.
  - When the user logs into the system via any SSO protocol (SAML 2.0, ODIC, WS-Federation), build the response with user attributes coming from multiple sources.

### Scenario
   - Mount the credential store and all the attribute stores as user stores to the WSO2 Identity Server. Follow a naming convention while naming the user stores where the attributes store can be differentiated from the credentials stores just by looking at the user store domain name.
   - Build a custom user store manager extension (extending the current user store manager corresponding to the type of the primary user store), which is aware of all the attribute stores in the system and override the method, which returns user attributes. The overridden method will iterate through the attribute stores find the user’s attributes and will return back the aggregated result.

When you are configuring the Attribute User store, you need to follow a special notation for the domain name.

Two simple rules to follow:
1. Domain must be same as the corresponding credentials store
2. Domain name must be qualified with a post prefix called   “-ATTRIBUTE-STORE”

The following diagram will explain the scenario in detail.

![alt text](src/test/resources/Solution27.png "Description goes here")


NOTE: 
1.This sample requires the application of config05. In both apply-config and revert-config set the mysqlJAR to the version of the mysql jar that will be used.
2.For 27-post-scenario-steps.sh please set the required values by export for 
serverHost
serverPort
tomcatHost
tomcatPort
tomcatUsername
tomcatPassword
JDBCUserStoreUrl
JDBCUserStoreUserName
JDBCUserStorePassword
LDAPUserStoreUrl
LDAPUserStoreConnPassword


### Pre - Requisites
1. Get a clone of the following repository and build
```sh 
https://github.com/dilinisg/attribute-store-extension 
```
2. Copy the created jar (org.soasecurity.user.mgt.attribute.store.extension-1.0.0.jar) into <IS_HOME>/repository/components/dropins directory
3. Copy the required DB drivers to <IS_HOME>/repository/components/lib directory
4. Restart the server
5. A Read Write LDAP should be available
6. Tomcat server should be up and running
7. Follow the steps in [1] and get a checkout of the travelocity sample and build
```sh 
[1]https://docs.wso2.com/display/IS540/Configuring+Single+Sign-On
```
8. Deploy a travelocity web app (travelocity.com.war) in tomcat. 
9. Change the configurations according to the environment in user.properties under scenario 27. (scenario27/src/test/resources/user.properties)

### Run the test
To run sthe olution 27, run the below command
```sh run-scenario.sh

```

### References
http://xacmlinfo.org/2015/03/03/configure-attribute-sources-with-wso2-identity-server/
