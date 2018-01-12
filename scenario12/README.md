Scenario 12  Claim mapper


Problem:

The claim dialect used by the service provider is not compatible with the default claim dialect used by the WSO2 Identity Server.
The claim dialect used by the federated (external) identity provider is not compatible with the default claim dialect used by the WSO2 Identity Server.


Scenario:

Represent all the service providers in the WSO2 Identity Server and configure the corresponding inbound authenticators (SAML, OpenID, OIDC, WS-Federation).
For each service provider define custom claims and map them to the WSO2 default claim dialect.
Represent all the identity providers in the WSO2 Identity Server and configure corresponding federated authenticators (SAML, OpenID, OIDC, WS-Federation).
For each identity provider define custom claims and map them to the WSO2 default claim dialect.

Products: WSO2 Identity Server 5.0.0+

Configurations

Deploy a travelocity web app (travelocity.com.war) in tomcat.
Take a copy of travelocity.com.war and rename it as sol12travelocity.com.war
Edit the travelocity.properties with correct values as given in its comments.
#URIs to skip SSOAgentFilter; comma separated values #Replace with travelocity app name SkipURIs=/sol12travelocity.com/index.jsp

#A unique identifier for this SAML 2.0 Service Provider application #Replace with Service provider entity ID SAML2.SPEntityId=sol12travelocity.com

#The URL of the SAML 2.0 Assertion Consumer #Replace with tomcat host and port SAML2.AssertionConsumerURL=http://192.168.57.31:8080/sol12travelocity.com/home.jsp

#The URL of the SAML 2.0 Identity Provider #Replace with IS host/port SAML2.IdPURL=https://is.dev.wso2.org/samlsso

Restart the tomcat or web app.
Go to scenario12/src/test/resources/user.properties file and do the configurations as below.

IS Server

host=< HOST NAME OF IS SERVER >

port=< PORT OF THE IS SERVER >

admin_username=< ADMIN USER NAME >

admin_password=< ADMIN PASSWORD >

SP

sp_name=sol12travelocity.com

Application Details

travelocityApp= < TRAVELOCITY APPLICATION NAME > E.g., sol12travelocity.com

travelocityIssuer= < ISSUER OF THE TRAVELOCITY APP > E.g., sol12travelocity.com

Tomcat

tomcatHost=< HOSTNAME OF THE TOMECAT > 192.168.57.31

#tomcatHost= localhost

tomcatPort= 8080

Run the test

To run scenario 12 run the below command.

mvn clean verify --fae



