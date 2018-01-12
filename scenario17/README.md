**Jmeter script available for solution17 on [1]**

**Prerequisites**

- oauth2-proxy.war deployed in WSO2 IS ($IS_HOME/repository/deployment/server/webapps).
- oauth_proxy.properties file deployed in WSO2 IS ($IS_HOME/repository/conf).
- Sol17amazon.war deployed in Tomcat server

**Steps of Script**

Scripts will be able to run for following:

- Creating user and role in WSO2 IS
- Creating Service Provider with OAuth 2.0 (code grant) inbound authenticator 
- Login to SPA (Sol17amazon)
- Once all above done users and SP will be clean out from IS

[1] https://medium.facilelogin.com/thirty-solution-patterns-with-the-wso2-identity-server-16f9fd0c0389
