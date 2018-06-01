# Scenario 21 - Enforce users to provide missing required attributes while getting JIT provisioned to the local system

### SCENARIO DESCRIPTION

##### Problem:

-The business users need to access multiple service providers via federated identity provider (i.e Facebook, Yahoo, Google).

-Need to JIT provision all the user coming from federated identity providers with a predefined set of attributes.

-If any required attributes are missing in the authentication response from the federated identity provider, the system should present a UI to the user to provide those.

############# Scenario:

- Deploy WSO2 Identity Server as the Identity Provider and register all the service providers and federated identity providers.
- Enable JIT provisioning for each federated identity provider.
- Build a connector to validate the attributes in the authentication response and compare those against the required set of attributes. The required set of attributes can be defined via a claim dialect. If there is a mismatch between the attributes from the authentication response and the required set of attributes then this connector will redirect the user to web page (deployed under authenticationendpoints web app) to accept the missing attributes from the user.
- Engage the attribute checker connector from the previous step to an authentication step after the step, which includes the federated authenticator.

#####  Pre - Requisites
- Tomcat should be configured with a user having specific permissions
ex:<user username="scriptuser" password="scriptuser" roles="manager-gui,admin-gui,manager-script"/>


##### Configurations
1. Follow the steps in this [1] and get a checkout of travelocity sample and build
    [1]https://docs.wso2.com/display/IS500/Configuring+Single+Sign-On+with+SAML+2.0#ConfiguringSingleSign-OnwithSAML2.0-Prerequisites
2. Deploy a travelocity web app (travelocity.com.war) in tomcat.
3. Change the configurations according to the environment in *user.properties* under *21*. (scenario21/src/test/resources/user.properties)
```sh
#Admin User information
admin_username=admin
admin_password=admin
admin_credentials=YWRtaW46YWRtaW4=

#Created User information
username=TestFBuser25
password=test12345#

#IDP information
FbIdentityProviderName=IDPfacebooktest3
FbClientId=486523028382606
FbSecret=05ca26f98f4a542e139d82153d90920a
FbCallbackUrl=https://localhost:443/commonauth
FbScope=email
FbUserInfoFields=id,name,gender,email,first_name,last_name,age_range,link

#server Information
serverHost=localhost
serverPort=9443

#Sp Information
spName=travelocity.com
spDescription=Configuringtravelocity
permission=/permission/admin
role=roleIDP21

#Tomcat server Information
tomcatHost=localhost
tomcatPort=8080
travelocityIssuer=travelocity.com
```
##### Run the test
To run scenario 21 run the below command.
```sh
mvn clean verify --fae
```
