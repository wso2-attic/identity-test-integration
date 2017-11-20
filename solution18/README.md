# Solution 18 - Fine-grained access control for service providers

### SOLUTION DESCRIPTION

##### Problem:

-The business users need to access multiple service providers supporting multiple heterogeneous identity federation protocols.

-Each service provider needs to define an authorization policy at the identity provider, to decide whether a given user is eligible to log into the corresponding service provider.

-For example, one service provider may have a requirement that only the admin users will be able to login into the system after 6 PM.

-Another service provider may have a requirement that only the users from North America should be able to login into the system.

##### Solution:

-Deploy WSO2 Identity Server as the Identity Provider and register all the service providers.

-Build a connector, which connects to the WSO2 Identity Server’s XACML engine to perform authorization.

-For each service provider, that needs to enforce access control during the login flow, engage the XACML connector to the 2nd authentication step, under the Local and Outbound Authentication configuration.

-Each service provider, that needs to enforce access control during the login flow, creates its own XACML policies in the WSO2 Identity Server PAP (Policy Administration Point).

-To optimize the XACML policy evaluation, follow a convention to define a target element under each XACML policy, that can uniquely identify the corresponding service provider.

Products: WSO2 Identity Server 5.0.0+

To run solution 18 run the below command.

```bash
mvn clean verify --fae
```

#### Configurations
1. Deploy a travelocity web app (travelocity.com.war) in tomcat.
2. Take a copy of travelocity.com.war and rename it as Sol18travelocity.com.war
3. Once the Sol18travelocity web app is deployed, replace the travelocity.properties with solution18/src/test/resources/travelocity.properties
4. Edit the travelocity.properties with correct values as given in its comments.

#URIs to skip SSOAgentFilter; comma separated values
#Replace with travelocity app name
SkipURIs=/Sol18travelocity.com/index.jsp


#A unique identifier for this SAML 2.0 Service Provider application
#Replace with Service provider entity ID
SAML2.SPEntityId=Sol18travelocity.com

#The URL of the SAML 2.0 Assertion Consumer
# Replace with tomcat host and port
SAML2.AssertionConsumerURL=http://192.168.57.31:8080/Sol18travelocity.com/home.jsp

#The URL of the SAML 2.0 Identity Provider
#Replace with IS host/port
SAML2.IdPURL=https://is.dev.wso2.org/samlsso


5. Restart the tomcat or web app.
6. Go to solution18/src/test/resources/user.properties file and do the configurations as below.

###### IS Server
host=< HOST NAME OF IS SERVER >

port=< PORT OF THE IS SERVER >

admin_username=< ADMIN USER NAME >

admin_password=< ADMIN PASSWORD >

###### SP
sp1=Sol18travelocity.com

###### Application Details

travelocityApp= < TRAVELOCITY APPLICATION NAME > E.g., Sol18travelocity.com

travelocityIssuer= < ISSUER OF THE TRAVELOCITY APP > E.g., Sol18travelocity.com

###### Tomcat
tomcat_host=< HOSTNAME OF THE TOMECAT >  192.168.57.31

#tomcat_host=<HOSTNAME OF THE TOMCAT >  localhost

tomcat_port= <PORT OF THE TOMCAT> 8080


