**Jmeter script available for scenario25 on [1]**

25.0 Fine-grained access control for SOAP services

Problem:

- Access to the business services must be done in a fine-grained manner.
- Only the users belong to the business-admin role should be able to access foo and bar SOAP services during a weekday from 8 AM to 5 PM.

Solution:

- Deploy WSO2 Identity Server as a XACML PDP (Policy Decision Point).
- Define XACML policies via the XACML PAP (Policy Administration Point) of the WSO2 Identity Server.
- Front the SOAP services with WSO2 ESB and represent each service a proxy service in the ESB.
- Engage the Entitlement mediator to the in-sequence of the proxy service, which needs to be protected. The Entitlement mediator will point to the WSO2 Identity Server’s XACML PDP.
- All the requests to the SOAP service will be intercepted by the Entitlement mediator and will talk to the WSO2 Identity Server’s XACML PDP to check whether the user is authorized to access the service.
- Authentication to the SOAP service should happen at the edge of the WSO2 ESB, prior to Entitlement mediator.
- If the request to the SOAP service brings certain attributes in the SOAP message itself, the Entitlement mediator can extract them from the SOAP message and add to the XACML request.

Products: WSO2 Identity Server 4.0.0+, WSO2 ESB, Governance Registry


**Prerequisites**

1. SimpleStockQuoteService is up and runing in axis2Server. 
2. EI is up and running. 
3. Upload the capp to WSO2 EI. (please find the capp at apps folder)
4. SimpleStockQuoteService is secured with a proxy. The proxy endpoint: https://localhost:8243/services/criticalillnessproxy 
5. Create two users in EI. sol25user(permitted user - sol25role) and fUser1(non permitted user - Finance)


**Steps of Script**

Scripts will be able to run for following:

- Creating users in WSO2 IS
- Add XACML policy and make IS as PDP
- EI up and running with entitlement mediator which is pointing to PDP in IS
- Invoke EI proxy with valid credentials for the scenario and it should invoke SOAP service
- Invoke EI proxy with non permitted user for the scenario and it should not invoke SOAP service
- Once all above done users and XACML policy will be clean out from IS

How to run:
1. Run the export command
export serverHost=localhost serverPort=9444 JMETER_HOME=/apache-jmeter-3.3 eiHost=localhost eiPort=8243

2. sh run-scenario.sh



[1] https://medium.facilelogin.com/thirty-solution-patterns-with-the-wso2-identity-server-16f9fd0c0389
