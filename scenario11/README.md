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
1. travelocity.com.war file is deployed in Tomcat with below configurations in travelocity.properties file. This is built from source in apps/ folder. 


#URIs to skip SSOAgentFilter; comma separated values
#Replace with travelocity app name
SkipURIs=/travelocity.com/index.jsp


#A unique identifier for this SAML 2.0 Service Provider application
#Replace with Service provider entity ID
SAML2.SPEntityId=travelocity.com

#The URL of the SAML 2.0 Assertion Consumer
#Replace with tomcat host and port
SAML2.AssertionConsumerURL=http://${tomcatHost}:${tomcatPort}/travelocity.com/home.jsp

#The URL of the SAML 2.0 Identity Provider
#Replace with IS host/port
SAML2.IdPURL=https://${isHost}/samlsso

2. PassiveSTSSampleApp.war file is deployed in tomcat with below configurations in web.xml file. This is built from source in apps/ folder. 
idpUrl - https://${isHost}:9443/passivests
replyUrl - http://${tomcatHost}:${tomcatPost}/PassiveSTSSampleApp/index.jsp
realm - PassiveSTSSampleApp

├── scenario11
│   ├── base-setup.sh
│   ├── jmeter
│   │   ├── 01-Scenario-11-Identity-federation-between-sps-and-idps.jmx
│   │   ├── YY-post-scenario-steps.sh
│   │   ├── YY-pre-scenario-steps.sh
│   │  
│   ├── README.md
│   ├── resources
│   │   |── user.properties
│   │── teardown.sh  
│      
│   

### Run it against the Testgrid 
1. export serverHost=localhost serverPort=9443 tomcatHost=localhost tomcatPort=8080
2. sh 29-pre-scenario-steps.sh
3. /path/to/apache-jmeter-3.2/bin/jmeter -n -t xxxx.jmx -p /path/to/user.properties -l xxxx.jtl
4. sh 29-post-scenario-steps.sh


