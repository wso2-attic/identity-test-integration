# Solution 28 - Home Relam Discovery

Following scenarios are covered through this automation script.

###### Problem:
- The business users need to login to multiple service providers via multiple identity providers.
- Rather than providing a multi-login option page with all the available identity provider, once redirected from the service provider, the system should find out who the identity provider corresponding to the user and directly redirect the user there.

###### Solution:
- Deploy WSO2 Identity Server as an identity provider and register all the service providers and identity providers.
- For each identity provider, specify a home realm identifier.
- The service provider prior to redirecting the user to the WSO2 Identity Server must find out the home realm identifier corresponding to the user and send it as a query parameter.
- Looking at the home realm identifier in the request the WSO2 Identity Server redirect the user to the corresponding identity provider.
- In this case, there is a direct one-to-one mapping between the home realm identifier in the request and the home realm identifier value set under the identity provider configuration.

###### Scenario Details 

Scenario 1 - Service Provide decided to authenticate with facebook, hence the service provider is sending a query param called "fidp" with the home realm identifier of an existing identity provider.
Scenario 2 - Multiple external identity providers configured for the Service Provider. If service provider does not send the required IDP with the "fidp" query param, all the configured IDPs will be provided as logging options

###### Pre - Requisites 

Note - You can have two differnt web applications for the positive and negative scenarios
1. Tomcat server should be up and running
2. Take a copy of travelocity.com.war and rename it as solution28travelocity.com.war for the positive scenario **with fidp query param**.
3. Change the following parameters according to the environment
```sh
#URIs to skip SSOAgentFilter; comma separated values
SkipURIs=/solution28travelocity.com/index.jsp

#A unique identifier for this SAML 2.0 Service Provider application
SAML2.SPEntityId=travelocitysolution28.com

#The URL of the SAML 2.0 Assertion Consumer
SAML2.AssertionConsumerURL=http://192.168.57.31:8080/solution28travelocity.com/home.jsp

#A unique identifier for this SAML 2.0 Service Provider application
SAML2.IdPEntityId=is.dev.wso2.org

#The URL of the SAML 2.0 Identity Provider
SAML2.IdPURL=https://is.dev.wso2.org/samlsso

#Additional request parameters
QueryParams=fidp=facebook
```
4. Take another copy of travelocity.com.war and rename it as negativesolution28travelocity.com.war for the scenario **when fidp query param is not defined**.
5. Change the following parameters according to the environement
```sh
#URIs to skip SSOAgentFilter; comma separated values
SkipURIs=/negativesolution28travelocity.com/index.jsp

#A unique identifier for this SAML 2.0 Service Provider application
SAML2.SPEntityId=negativesolution28travelocity.com

#The URL of the SAML 2.0 Assertion Consumer
SAML2.AssertionConsumerURL=http://192.168.57.31:8080/negativesolution28travelocity.com/home.jsp

#A unique identifier for this SAML 2.0 Service Provider application
SAML2.IdPEntityId=is.dev.wso2.org

#The URL of the SAML 2.0 Identity Provider
SAML2.IdPURL=https://is.dev.wso2.org/samlsso
```
6. Deploy the above two web applications in the tomcat server


