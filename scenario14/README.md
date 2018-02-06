# Scenario 14 - Enforce password reset for expired passwords during the authentication flow

### SCENARIO DESCRIPTION

##### Problem:

- During the authentication flow, enforce to check whether the end-user password is expired and if so, prompt the user to change the password.


##### Scenario:

-   Configure multi-step authentication for the corresponding service provider.
-   Engage basic authenticator for the first step, which accepts username/password from the end-user.
-   Write a handler (a local authenticator) and engage it in the second step, which will check the validity of the user’s     password and if it is expired then prompt the user to reset the password.
    Sample implementation: http://blog.facilelogin.com/2016/02/enforce-password-reset-for-expired.html
    Alternatively you can use the connector and configure it withoug writing a custom handler as mentioned in https://docs.wso2.com/display/ISCONNECTORS/Password+Policy+Authenticator

Products: WSO2 Identity Server 5.0.0+


### Configurations
1. Follow the steps in this [1] and get a checkout of travelocity sample and build it
svn co http://svn.wso2.org/repos/wso2/carbon/platform/branches/turing/products/is/5.0.0/modules/samples/sso/
[1]https://docs.wso2.com/display/IS500/Configuring+Single+Sign-On+with+SAML+2.0#ConfiguringSingleSign-OnwithSAML2.0-Prerequisites
2.  Deploy a travelocity web app (travelocity.com.war) in tomcat.
3. Copy the pwd-reset.jsp to <IS_HOME>/repository/deployment/server/webapps/authenticationendpoint ( please note that IS needs to be started atleast ones to perform this step
4. Copy the org.wso2.carbon.extension.identity.authenticator.passwordpolicy.connector-1.0.3.jar to  <IS_HOME>/repository/components/dropins
5. Set the property Authentication.Policy.Password.Reset.Time.In.Days=20 in identity-mgt.properties found in the <IS_HOME>/repository/conf/identity



### Run the test

Configure the user.properties and run the below command to execute the script.

```bash
path/to/jmeter/bin/jmeter -n -t path/to/01-Scenario14-EnforcePasswordReset.jmx -p path/to/user.properties -l xxxx.jtl
```

