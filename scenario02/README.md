# Scenario 2 - Multiple login options by service provider
Following scenarios are covered through this automation script.

##### Problem:
  - The business users need to access multiple service providers, where each service provider requires different login options. For example login to Google Apps with username/password, while login to Drupal either with username/password or Facebook
 - Enable multi-factor authentication for some service providers. For example login to Salesforce require username/password + FIDO.

##### Scenario:
  - Deploy WSO2 Identity Server over the enterprise user store.
  - Represent each service providers in Identity Server and under each service provider, configure local and outbound authentication options appropriately. To configure multiple login options, define an authentication step with the required authenticators.
  - When multi-factor authentication is required, define multiple authentication steps having authenticators, which support MFA in each step. For example username/password authenticator in the first step and the FIDO authenticator in the second step.
  - If federated authentication is required, for example, login with Facebook, represent all federated identity providers in Identity Server, as Identity Providers and engage them with appropriate service providers under the appropriate authentication step.
  - In each service provider, configure WSO2 Identity Server as a trusted identity provider. For example in Google Apps, add WSO2 Identity Server as a trusted identity provider.
##### Scenario Details
- Scenario 1 - Multi Factor Authenticator with Basic authentication and Facebook as a federated authenticator.
- Scenario 2 - IS as a federated authenticator.

#####  Pre - Requisites
- Tomcat server should be up and running
- A seperate Identitiy Server should be up and running.

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
tomcatHost=192.168.57.31
tomcatPort=8080

# User Management
adminUsername=<Admin username of IS server>
adminPassword=<Admin password of IS server>

# IDP
FbIdentityProviderName=<Facebook IDP name>
FbIdentityProvider_description=<Facebook IDP description>
GoogleIdentityProviderName=<Google IDP name>
GoogleIdentityProvider_description=<Google IDP description>

# SP
spName=<Facebook SP name>
spDescription=<Facebook SP description>
travelocityIssuer=<Facebook Issuer>
GoogleSPName=<Google SP name>
GtravelocityIssuer=<Google Issuer>

#Facebook
Fusername=<Username for user creation for Facebook> 
Fpassword=<Password for user creation for Facebook> 
role=<Role name for role creation for Facebook>
permission=<Permission for role>
FbClientId=<Username from the Facebook app>
FbSecret=<Password from the Facebook app>
FbCallbackUrl=<URL to which the browser should be redirected after the authentication is successful>
FbScope=<Restrict the claims sent to the Identity Serve>
FbUserInfoFields=<list of claims that you need to receive>

#ISasIDP

ISIdentityProviderName=Secondary
serverHostSecondary=<Hostname of the Secondary IS server>
serverPortSecondary=9443
serverSSOurlSecondary=samlsso
ISIdPEntityId=Secondary IDP
ISSPEntityId=Primary
secondarySPName=PrimaryIDP
secondaryspDescription=PrimaryIDP
Primaryissuer=Primary
SPNamePrimary=Travelocity
SPDescriptionPrimary=Travelocity as the SP in the primary IS
alias=oauth2/token
secondaryUsername=testUser
secondaryPassword=testUser_123
secondaryIncorrectPassword=testUser_456
adminUsernameSecondary=admin
adminPasswordSecondary=admin
```
##### Run the test
To execute the scenario 02, run the below command inside the scenario folder.
```sh
sh run-scenario.sh
```
