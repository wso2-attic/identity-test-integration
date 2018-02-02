# Scenario 11 - Identity federation between service providers and identity providers with incompatible identity federation protocols

### SCENARIO DESCRIPTION

##### Problem:

-The business users need to login into a SAML service provider with an assertion coming from an OpenID Connect identity provider.

-In other words, the user is authenticated against an identity provider, which only supports OpenID Connect, but the user needs to login into a service provider, which only supports SAML 2.0.


##### Scenario:

-Represent all the service providers in the WSO2 Identity Server and configure the corresponding inbound authenticators (SAML, OpenID, OIDC, WS-Federation).

-Represent all the identity providers in the WSO2 Identity Server and configure corresponding federated authenticators (SAML, OpenID, OIDC, WS-Federation).

-Associate identity providers with service providers, under the Service Provider configuration, under the Local and Outbound Authentication configuration, irrespective of the protocols they support.

Products: WSO2 Identity Server 5.0.0+


### Configurations
1. Follow the steps in this [1] and get a checkout of travelocity sample and build it
svn co http://svn.wso2.org/repos/wso2/carbon/platform/branches/turing/products/is/5.0.0/modules/samples/sso/
[1]https://docs.wso2.com/display/IS500/Configuring+Single+Sign-On+with+SAML+2.0#ConfiguringSingleSign-OnwithSAML2.0-Prerequisites
2.  Deploy a travelocity web app (travelocity.com.war) in tomcat.
3. Take a copy of travelocity.com.war and rename it as Sol11travelocity.com.war if you are goin gto customise it as Sol11travelocity.com.war. Otherwise you can continue with step 5.
4. Once the Sol11travelocity web app is deployed, replace the travelocity.properties with scenario18/src/test/resources/travelocity.properties
5. Edit the travelocity.properties with correct values as given in its comments.

#URIs to skip SSOAgentFilter; comma separated values
#Replace with travelocity app name
SkipURIs=/Sol11travelocity.com/index.jsp


#A unique identifier for this SAML 2.0 Service Provider application
#Replace with Service provider entity ID
SAML2.SPEntityId=Sol11travelocity.com

#The URL of the SAML 2.0 Assertion Consumer
#Replace with tomcat host and port
SAML2.AssertionConsumerURL=http://192.168.57.31:8080/Sol11travelocity.com/home.jsp

#The URL of the SAML 2.0 Identity Provider
#Replace with IS host/port
SAML2.IdPURL=https://is.dev.wso2.org/samlsso

5. Restart the tomcat or web app.
6. Go to scenario11/src/test/resources/user.properties file and do the configurations as below.

###### IS Server
host=< HOST NAME OF IS SERVER >

port=< PORT OF THE IS SERVER >

admin_username=< ADMIN USER NAME >

admin_password=< ADMIN PASSWORD >

##### SP
sp1=Sol11travelocity.com

##### Application Details

travelocityApp= < TRAVELOCITY APPLICATION NAME > E.g., Sol11travelocity.com

travelocityIssuer= < ISSUER OF THE TRAVELOCITY APP > E.g., Sol11travelocity.com

##### Tomcat
tomcatHost=< HOSTNAME OF THE TOMECAT >  192.168.57.31

#tomcatHost=<HOSTNAME OF THE TOMCAT >  localhost

tomcatPort= <PORT OF THE TOMCAT> 8080

### Run the test

To run scenario 11 run the below command.

```bash
mvn clean verify --fae
```

