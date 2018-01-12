**Jmeter scripts are available for Request Path Authenticator scenario which explained in scenario23 on [1]**

Scripts will be able to run for following accordingly:

1. Script I - [scenario23.jmx]

It is written to cover "basic-auth" Request path authenticator option
- Registering Service Providers for web apps (e.g. travelocity.com and avis.com)
- Add SAML SSO inbound configuration for both SPs
- Add 'Basic Auth Request Path Authenticator' for a legacy webapp (e.g. travelocity.com)
- Invoke the samlsso endpoint with a SAML Request using sectoken
- Access second SP with automatically authenticated, as the previous step created a web session for the logged in user
- Once all above done user will un-deploy the SPs

2. Script II - [scenario23_B.jmx]

It is written to cover "oauth-bearer" Request path authenticator option
- Registering a Service Provider OAuth app 
- Add OAuth/Open ID Connect configuration for above SP
- Add 'OAuth Request Path Authenticator' for a above SP
- Request to the token endpoint to recieve an OAuth token for above app using any grant-type (default with password)
- Request to the authorize endpoint to recieve authorization code 
- Invoke the token endpoint to generate an access token to access the application by using the recieved code & recieved OAuth token on above steps

**Request path authenticator**

Using request path authenticator to authenticate requests that contain the user’s credentials, which means that you can use the Single-Sign-On mechanism without having an identity provider login page to prompt the end user for credentials. Figure shows how request path authenticator works.

![alt text](https://github.com/kavithasub/identity-test-integration/blob/master/scenario23/req.path.auth.png)

***authentication request that contain the user’s credentials.*

[1] https://medium.facilelogin.com/thirty-solution-patterns-with-the-wso2-identity-server-16f9fd0c0389
