# Solution 05 - Multi-factor authentication for WSO2 Identity Server management console

## SOLUTION DESCRIPTION

### Problem:

-Enable MFA for the WSO2 Identity Server Management Console.

-In other words, the Identity Server’s Management Console itself must be protected with MFA.


### Solution:

-Introduce WSO2 Identity Server as a service provider to itself.

-Under the service provider configuration, configure multi-step authentication having authenticators, which support MFA in each step.

-Enable SAML SSO carbon authenticator through the corresponding configuration file.

Products: WSO2 Identity Server 5.0.0+


### Configurations

1. Go to solution05/src/test/resources/user.properties file and change the values of configurations as below.

#### IS Server
serverHost=< HOST NAME OF IS SERVER > <br />
serverPort=< PORT OF THE IS SERVER > <br />


#### User Management
adminusername=< ADMIN USER NAME > <br />
adminpassword=< ADMIN PASSWORD > <br />
adminCredentials=< BASE64 Encoded ADMIN USERNAME:ADMIN PASSWORD > <br />
rolename= < NEW ADMIN ROLE NAME > <br />
usernamePrefix=< NEW ADMIN USERNAME > <br />
noOfUsers= < NUMBER OF USERS TO CREATE > <br />


#### IDP
idpname=< IDP NAME > <br />
idpdescription=< IDP DESCRIPTION > <br />
fbclientID= < CLIENT ID OF fACEBOOK APPLICATION > <br />
fbclientSecret= < CLIENT SECRET OF fACEBOOK APPLICATION > <br />


#### SP
spname=< SP NAME > <br />
spdescription=< SP DESCRIPTION > <br />
carbonServer=< ISSUER NAME > <br />


#### TestConfigs
fbserver=facebook.com <br />
redirect=commonauth <br />
FBLogin_Email= < EMAIL ADDRESS OF AUTHORIZED FB USER > <br />
FBUsername= < USERNAME OF AUTHORIZED FB USER > <br />
FBPassword= < PASSWORD OF AUTHORIZED FB USER > <br />


#### How to Run

To try out the solution 05, run the below command.

```bash
mvn clean verify --fae
```

