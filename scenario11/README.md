Solution 11  Identity federation between service providers and identity providers with incompatible identity federation protocols


Problem:

ness users need to login into a SAML service provider with an assertion coming from an OpenID Connect identity provider.
In other words, the user is authenticated against an identity provider, which only supports OpenID Connect, but the user needs to login into a service provider, which only supports SAML 2.0.


Solution:

Represent all the service providers in the WSO2 Identity Server and configure the corresponding inbound authenticators (SAML, OpenID, OIDC, WS-Federation).
Represent all the identity providers in the WSO2 Identity Server and configure corresponding federated authenticators (SAML, OpenID, OIDC, WS-Federation).
Associate identity providers with service providers, under the Service Provider configuration, under the Local and Outbound Authentication configuration, irrespective of the protocols they support.

Products: WSO2 Identity Server 5.0.0+



In the provided solution script, following value set and happy/unhappy paths are included. 
#Service Provider 1(SAML2) - Travelocity
#Fedarated Authenticators - Facebook, Twitter

#Service Provider 2(WS-Federation - Passive) - STS web app
#Fedarated Authenticators - Twitter

#Negative Scenario - Login to Travelocity with Facebook credentials when the client ID is incorrect. 



Configurations

1. Deploy a travelocity web app (travelocity.com.war) in tomcat. 
2. Deploy STS web App in tomcat. (warfile can be found in /identity-test-integration/solution11/src/test/resources folder)
Place PassiveSTSSampleApp.war file in tomcat/webapps folder. In /PassiveSTSSampleApp/WEB-INF/web.xml file do the following changes. 

	idpUrl=https://localhost:9443/passivests
	replyUrl=http://<tomcatHost>:8080/PassiveSTSSampleApp/index.jsp
	realm=PassiveSTSSampleApp (This should be the same valus as inboundAuthKey value in 'Update SP2 with IDP3 Twiiter' section in Jmeter script)


3. Since this solution uses Selenium inside the JMETER place the relavent jars as described below.
plugins-manager.jar -> Jmeter/lib/ext  
Selenium Standalone Server.jar -> Jmeter/lib  