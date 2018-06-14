**Jmeter script available for solution17 on [1]**

**Prerequisites**

- oauth2-proxy.war deployed in WSO2 IS ($IS_HOME/repository/deployment/server/webapps).
- oauth_proxy.properties file deployed in WSO2 IS ($IS_HOME/repository/conf).
- Sol17amazon.war deployed in Tomcat server

**Special NOTE**
This script does not navigate through the user consent flow scince when the apply-config.sh is run the SkipUserConsent is set to false. The jmeter script flow assumes that the consent flow does not occur.

**Scenario**
This script will create a user and a service provider. Next the the Single Page Application will be accessed and the user credentials will be submitted for the user to login. In this scenario we keep the SkipUserConsent to true when the apply-config.sh is invoked so that the user does not need to grant consent for the single page application.

**Steps of Script**
1.Invoke the apply-config.sh to update the identity server

2.Invoke the run-scenario.sh
2.1.The first call will update the tomcat with the Sol17amazon.war.
2.2.The second scenario will create a user and then submit the user credentials to the index.html. This will direct the user to authentication endpoint and once validated, the user will be redirected to in.html. 
2.3.The thrid call will be to undeploy the Sol17amazon from tomcat.

3.Finaly we run the revert-config.sh, this configurations applied in step1 will be revered 

Scripts will be able to run for following:

- Creating user and role in WSO2 IS
- Creating Service Provider with OAuth 2.0 (code grant) inbound authenticator 
- Login to SPA (Sol17amazon) and assert if the logout link is provided on in.html
- Once all above done users and SP will be clean out from IS

[1] https://medium.facilelogin.com/thirty-solution-patterns-with-the-wso2-identity-server-16f9fd0c0389
