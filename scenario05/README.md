# Scenario 05 - Multi-factor authentication for WSO2 Identity Server management console

## SOLUTION DESCRIPTION

### Problem:

-Enable MFA for the WSO2 Identity Server Management Console.
-In other words, the Identity Server’s Management Console itself must be protected with MFA.


### Scenario:
-Introduce WSO2 Identity Server as a service provider to itself.
-Under the service provider configuration, configure multi-step authentication having authenticators, which support MFA in each step.
-Enable SAML SSO carbon authenticator through the corresponding configuration file.

Products: WSO2 Identity Server 5.0.0+


### Configurations

1. Go to scenario05/src/test/resources/user.properties file and change the values of configurations as below.
2. Go to /config-sets/config02 and run apply-config.sh
3. Go to /config-sets/config02 and run config-init.sh

#### IS Server
serverHost=< HOST NAME OF IS SERVER >
serverPort=< PORT OF THE IS SERVER > 


#### User Management
adminusername=< ADMIN USER NAME > 
adminpassword=< ADMIN PASSWORD > 
adminCredentials=< BASE64 Encoded ADMIN USERNAME:ADMIN PASSWORD >
rolename= < NEW ADMIN ROLE NAME > 
usernamePrefix=< NEW ADMIN USERNAME > 
noOfUsers= < NUMBER OF USERS TO CREATE > 
testuserpass=sol5admin1
testAdminCredentials=c29sNWFkbWluMTphZG1pbg==

#### IDP
idpname=< IDP NAME >
idpdescription=< IDP DESCRIPTION >
fbclientID= < CLIENT ID OF fACEBOOK APPLICATION >
fbclientSecret= < CLIENT SECRET OF fACEBOOK APPLICATION >


#### SP
spname=< SP NAME >
spdescription=< SP DESCRIPTION >
carbonServer=< ISSUER NAME > 


#### TestConfigs
fbserver= facebook.com
redirect=commonauth
FBLogin_Email= < EMAIL ADDRESS OF AUTHORIZED FB USER >
FBUsername= < USERNAME OF AUTHORIZED FB USER >
FBPassword= < PASSWORD OF AUTHORIZED FB USER >
twitterUserName= < USERNAME OF AUTHORIZED Twitter USER >
twitterPassword= < PASSWORD OF AUTHORIZED Twitter USER >

##### Run the test
To execute the scenario 05, run the below command inside the scenario folder.
```sh
sh run-scenario.sh
```
##### Post-Requisites
1. Go to /config-sets/config02 and run revert-config.sh

