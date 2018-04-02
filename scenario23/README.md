**Jmeter scripts are available for Request Path Authenticator scenario which explained in pattern23 in blog post[1]**

Scripts will be able to run for following accordingly:

1. Scripts[ '01-Scenario-23-BasicAuthRequestPathAuthenticator-RegisterTravelocityApp.jmx' , '02-Scenario-23-BasicAuthRequestPathAuthenticator-RegisterAvisApp.jmx' , '03-Scenario-23-BasicAuthRequestPathAuthenticator-LegacyAppLogin.jmx']

Scripts created to cover "basic-auth" Request path authenticator option as following
- Registering Service Providers for web apps (e.g. travelocity.com and avis.com)
- Add SAML SSO inbound configuration for both SPs
- Add 'Basic Auth Request Path Authenticator' for a legacy webapp (e.g. travelocity.com)
- Invoke the samlsso endpoint with a SAML Request using sectoken
- Access second SP with automatically authenticated, as the previous step created a web session for the logged in user
- Once all above done user will un-deploy the SPs

2. Scripts[ '04-Scenario-23-OAuthBearerRequestPathAuthenticator-RegisterOAuthApp.jmx' , '05-Scenario-23-OAuthBearerRequestPathAuthenticator-Login.jmx'] 

Scripts created to cover "oauth-bearer" Request path authenticator option as following
- Registering a Service Provider OAuth app 
- Add OAuth/Open ID Connect configuration for above SP
- Add 'OAuth Request Path Authenticator' for a above SP
- Request to the token endpoint to recieve an OAuth token for above app using any grant-type (default with password)
- Request to the authorize endpoint to recieve authorization code 
- Invoke the token endpoint to generate an access token to access the application by using the recieved code & recieved OAuth token on above steps

3. Scripts['06-Scenario-23-OAuthBearerRequestPathAuthenticator-Negative1.jmx' , '07-Scenario-23-OAuthBearerRequestPathAuthenticator-Negative2.jmx']

Scripts created to cover some negative test cases with value set using "oauth-bearer" Request path authenticator option 

4. Scripts['10-Scenario-23-RemoveSps.jmx']

This is to remove all registered service providers for this scenario only.


**Request path authenticator**

Using request path authenticator to authenticate requests that contain the user’s credentials, which means that you can use the Single-Sign-On mechanism without having an identity provider login page to prompt the end user for credentials. Figure shows how request path authenticator works.

![alt text](scenario23/req.path.auth.png)
***authentication request that contain the user’s credentials.*

[1] https://medium.facilelogin.com/thirty-solution-patterns-with-the-wso2-identity-server-16f9fd0c0389

