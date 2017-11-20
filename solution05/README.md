# Solution 18 - Multi-factor authentication for WSO2 Identity Server management console

## SOLUTION DESCRIPTION

### Problem:

-The business users need to access multiple service providers supporting multiple heterogeneous identity federation protocols.

-Each service provider needs to define an authorization policy at the identity provider, to decide whether a given user is eligible to log into the corresponding service provider.

-For example, one service provider may have a requirement that only the admin users will be able to login into the system after 6 PM.

-Another service provider may have a requirement that only the users from North America should be able to login into the system.


### Solution:

-Introduce WSO2 Identity Server as a service provider to itself.

-Under the service provider configuration, configure multi-step authentication having authenticators, which support MFA in each step.

-Enable SAML SSO carbon authenticator through the corresponding configuration file.

Products: WSO2 Identity Server 5.0.0+


### Configurations

1. Go to solution05/src/test/resources/user.properties file and change the values of configurations as below.

#### IS Server
is_host=< HOST NAME OF IS SERVER >
is_port=< PORT OF THE IS SERVER >


#### User Management
adminusername=< ADMIN USER NAME >
adminpassword=< ADMIN PASSWORD >
adminCredentials=< BASE64 Encoded ADMIN USERNAME:ADMIN PASSWORD >
rolename= < NEW ADMIN ROLE NAME >
usernamePrefix=< NEW ADMIN USERNAME >
noOfUsers= < NUMBER OF USERS TO CREATE >


#### IDP
idp_name=< IDP NAME >
idp_description=< IDP DESCRIPTION >
fb_clientID= < CLIENT ID OF fACEBOOK APPLICATION >
fb_clientSecret= < CLIENT SECRET OF fACEBOOK APPLICATION >

#### SP
sp_name=< SP NAME >
sp_description=< SP DESCRIPTION >
carbonServer=< ISSUER NAME >

#### TestConfigs
fbserver=facebook.com
redirect=commonauth
FBLogin_Email= < EMAIL ADDRESS OF AUTHORIZED FB USER >
FB_Username= < USERNAME OF AUTHORIZED FB USER >
FB_Password= < PASSWORD OF AUTHORIZED FB USER >


#### How to Run

To thry out the solution 05, run the below command.

```bash
mvn clean verify --fae
```

