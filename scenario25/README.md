**Jmeter script available for scenario25 on [1]**

**Prerequisites**

- Script assume EI up and running with relevant proxy services.
- Script assume backend (axis2Server) up and running.

**Steps of Script**

Scripts will be able to run for following:

- Creating users in WSO2 IS
- Add XACML policy and make IS as PDP
- EI up and running with entitlement mediator which is pointing to PDP in IS
- Invoke EI proxy with valid credentials for the scenario and it should invoke SOAP service
- Invoke EI proxy with invalid credentials for the scenario and it should not invoke SOAP service
- Once all above done users and XACML policy will be clean out from IS

**Special Notes**

This will be going to validate XACML policy which will allow users between 9 am - 5 pm in IST time zone. This test case may fail due to different time zones. Please note that.

[1] https://medium.facilelogin.com/thirty-solution-patterns-with-the-wso2-identity-server-16f9fd0c0389
