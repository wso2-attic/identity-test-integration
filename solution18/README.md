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

Go to solution18/src/test/resources/user.properties file and do the configurations as below.

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


