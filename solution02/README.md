# Solution 2 - Multiple login options by service provider
Following scenarios are covered through this automation script.

##### Problem:
  - The business users need to access multiple service providers, where each service provider requires different login options. For example login to Google Apps with username/password, while login to Drupal either with username/password or Facebook
 - Enable multi-factor authentication for some service providers. For example login to Salesforce require username/password + FIDO.

##### Solution:
  - Deploy WSO2 Identity Server over the enterprise user store.
  - Represent each service providers in Identity Server and under each service provider, configure local and outbound authentication options appropriately. To configure multiple login options, define an authentication step with the required authenticators.
  - When multi-factor authentication is required, define multiple authentication steps having authenticators, which support MFA in each step. For example username/password authenticator in the first step and the FIDO authenticator in the second step.
  - If federated authentication is required, for example, login with Facebook, represent all federated identity providers in Identity Server, as Identity Providers and engage them with appropriate service providers under the appropriate authentication step.
  - In each service provider, configure WSO2 Identity Server as a trusted identity provider. For example in Google Apps, add WSO2 Identity Server as a trusted identity provider.
##### Scenario Details
- Scenario 1 - Facebook as a federated authenticator.
- Scenario 2 - Google as a federated authenticator.

#####  Pre - Requisites
- Tomcat server should be up and running
-  Set the below property, inorder to access admin services in WSO2 IS product.
```sh
<HideAdminServiceWSDLs> element to false in the <PRODUCT_HOME>/repository/conf/carbon.xml file.
```
##### Configurations
1. Follow the steps in this [1] and get a checkout of travelocity sample and build
    [1]https://docs.wso2.com/display/IS500/Configuring+Single+Sign-On+with+SAML+2.0#ConfiguringSingleSign-OnwithSAML2.0-Prerequisites
2. Deploy a travelocity web app (travelocity.com.war) in tomcat.
3.Change the configurations according to the environment in *user.properties* under *solution02*. (solution02/src/test/resources/user.properties)
```sh
#server
server_host=<HOST NAME OF IS SERVER >
server_port=443
admin_username=admin
admin_password=admin

# User Management
adminUsername=admin
adminPassword=admin

# IDP
idp_name=solution2FacebookIDP1
idp_description=solution2FacebookIDP1
GoogleIdentityProviderName=solution2GoogleIDP1
GoogleIdentityProvider_description=solution2GoogleIDP1

# Tomcat
tomcat_host=192.168.57.31
tomcat_port=8080

# SP
spName=travelocity.com
spDescription=travelocity
travelocityIssuer=travelocity.com
GoogleSPName=travelocity.com
GtravelocityIssuer=travelocity.com
Gpermission=/permission/admin
Grole=roleFacebook
permission=/permission/admin

#Facebook
Fusername=testuserFacebook
Fpassword=facebook123
FbIdentityProviderName=FacebookIdpsolution2
FbClientId=1523286427713552
FbSecret=895da2dfbb8d5437de8fcbc8f7c21e93
FbCallbackUrl=https://is.dev.wso2.org:443/commonauth
FbScope=email
FbUserInfoFields=id,name,gender,email,first_name,last_name,age_range,link

#Google
Gusername=testuserGoogle
Gpassword=google123
Alias=oauth2/token
GoogleClientId=1034373765339-gdvfue2smv2s7vtipjebp1ucek7a5ges.apps.googleusercontent.com
GoogleSecret=vpm0YMUljMQHntvKs2ZGJvDe
GoogleCallbackUrl=commonauth
Googlescope	scope=openid email profile
```
##### Run the test
To run solution 02 run the below command.
```sh
mvn clean verify --fae
```