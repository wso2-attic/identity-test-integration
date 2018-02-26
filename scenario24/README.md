# 24.0: Render menu items in a web app based on the logged-in user’s fine-grained permissions


##Problem:

- When a business user logs into a web app, the menu items in the web app should be rendered dynamically based on the user’s permissions.
- There can be a case if the same user logs at 9 AM and then again at 9 PM could see different menu items as the permission can also be time sensitive.
- There can be a case if the same user logs in from China and then again from Canada could see different menu items as the permission can also be location sensitive.

##Solution:

- Deploy WSO2 Identity Server as a XACML PDP (Policy Decision Point).
- Define XACML policies via the XACML PAP (Policy Administration Point) of the WSO2 Identity Server.
- When a user logs into the web app, the web app will talk to the WSO2 Identity Server’s XACML PDP endpoint with a XACML request using XACML multiple decision profile and XACML multiple resource profile.
- After evaluating the XACML policies against the provided request, the WSO2 Identity Server returns back the XACML response, which includes the level permissions the user has on each resource under the parent resource specified in the initial XACML request. Each menu item is represented as a resource in the XACML policy.
- The web app caches the decision to avoid further calls to the XACML PDP.
- Whenever some event happens at the XACML PDP side, which requires expiring the cache, the WSO2 Identity Server will notify a registered endpoint of the web app.


##Scenario Automation:


Scripts provide the testcases to covere the following.
- XAXML policy creation with domain, time and role base rules.
- Publish XACML policy
- Evaluate the policy

##How to run the scenario

1. Run 24-pre-scenario-steps.sh \
**Note:** External parameters, $serverHost and $serverPort should be provided when run the above script

2. Run the 01-Scenario24-XACML.jmx jmeter test plan.
```sh
><jmeter_home>/bin/jmeter -n -t 01-Scenario24-XACML.jmx -p ../resources/user.properties -l sceanario24Resutls.jtl
```
3. Run 24-post-scenario-steps.sh \


