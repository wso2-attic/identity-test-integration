# Scenario 10 - Single Sign On with delegated access control

##### Problem:
 - The business users need to login into multiple service providers with single sign on via an identity provider.
 - Some service providers may need to access backend APIs on behalf of the logged in user. For example, a user logs into the Cute-Cup-Cake-Factory service provider via SAML 2.0 web SSO and then the service provider (Cute-Cup-Cake-Factor) needs to access user’s Google Calendar API on behalf of the user to schedule the order pickup.

##### Scenario:
  - Represent all the service provider in the WSO2 Identity Server as Service Providers and configure inbound authentication appropriately either with SAML 2.0 or OpenID Connect.
  - For each service provider that needs to access backend APIs, configure OAuth 2.0 as an inbound authenticator, in addition to the SSO protocol (SSO protocol can be SAML 2.0 or OpenID Connect).
  - Once a user logs into the service provider, either via SAML 2.0 or OpenID Connect, use the appropriate grant type (SAML grant type for OAuth 2.0 or JWT grant type for OAuth 2.0) to exchange the SAML or the JWT token for an access token, by talking to the token endpoint of the WSO2 Identity Server.

##### Scenario Details
- Scenario 1 - SAML2 Bearer Assertion Profile of OAuth 2.0 with WSO2 Travelocity to retreive access token.
- Scenario 2 (Negative)- Incorrect Credentials Provided To Get Token.
- Scenario 3 (Negative)- Try To Get The Token After Logging Out.

#####  Pre - Requisites
- Tomcat server should be up and running
- Need to export several parameters with values before running the run-scenario.sh script
= export serverHost=[HostNameOfThePrimaryISServer] serverPort=[PortOfThePrimaryISServer] tomcatHost=[HostNameOfTomcatServer] tomcatPort=[PortOfTomcatServer] tomcatUsername=[TomcatUsername] tomcatPassword=[TomcatPassword] 

##### Configurations
1. Follow the steps in this [1] and get a checkout of travelocity sample and build 
    [1]https://docs.wso2.com/display/IS500/Configuring+Single+Sign-On+with+SAML+2.0#ConfiguringSingleSign-OnwithSAML2.0-Prerequisites
2. Deploy a travelocity web app (travelocity.com.war) in tomcat.
3.Change the configurations according to the environment in *user.properties* under *scenario02*. (scenario02/src/test/resources/user.properties).
```sh
#server
scriptHost=<Host name of IS server>
serverPort=<Port name of IS server>

# Tomcat
tomcatHost=<Host name of Tomcat server>
tomcatPort=<Port name of Tomcat server>

# User Management
adminUsername=<Admin username of IS server>
adminPassword=<Admin password of IS server>
role=adminRole
permission=/permission/admin
newUsername=s11user
newPassword=s11user
incorrectPassword=s11user11
scriptPath=<ScriptPath>

# SP
spName=<SP name>
spDescription=Sol 10 Service Provider
issuer=<Travelocity Issuer>
oauthConsumerKey=<Outh Consumer Key>
oauthConsumerSecret=<Outh Consumer Secret>

```
##### Run the test
To execute the scenario 02, run the below command inside the scenario folder.
```sh
sh run-scenario.sh
```
