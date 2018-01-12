# Scenario 28 - Home Relam Discovery

Following scenarios are covered through this automation script.

### Problem:
- The business users need to login to multiple service providers via multiple identity providers.
- Rather than providing a multi-login option page with all the available identity provider, once redirected from the service provider, the system should find out who the identity provider corresponding to the user and directly redirect the user there.

### Solution:
- Deploy WSO2 Identity Server as an identity provider and register all the service providers and identity providers.
- For each identity provider, specify a home realm identifier.
- The service provider prior to redirecting the user to the WSO2 Identity Server must find out the home realm identifier corresponding to the user and send it as a query parameter.
- Looking at the home realm identifier in the request the WSO2 Identity Server redirect the user to the corresponding identity provider.
- In this case, there is a direct one-to-one mapping between the home realm identifier in the request and the home realm identifier value set under the identity provider configuration.

## Scenario Coverage

Following sub scenarios are covered in the automation script

- Scenario 1 - Identify the IDP corresponding to the fidp using the Home Realm identifier and authenticate with the IDP.

- Scenario 2 - If there is no IDP corresponding to the fidp, An option should be given to the user to provide a valid fidp

- Scenario 3 - If there is no IDP corresponding to the fidp an option is provided to the user to enter a valid fidp. Once the user provides a valid fidp, user should be able to get authenticated via the IDP.

- Scenario 4 - When the Home Realm identifier of the IDP contains special charachters, Still the user should be able to get authenticated via the IDP corresponding to the fidp.

- Scenario 5 - User should be able to define an identifier for the Resident IDP, and authenticate via Resident IDP

## Executing the Scenario 

Export input variables in the terminal
**>>export serverHost=<is_host> serverPort=<is_port> tomcatHost=<tomcatHost> tomcatPort=<tomcatPort>**
Ex:
```
>>export serverHost=is.localtest.com serverPort=9454 tomcatHost=localhost tomcatPort=8090
```
Update below two lines in the base-setup.sh and teardown.sh as replaccing values with your tomact user/password.
```
tomcatUsername=<username>
tomcatPassword=<password>
```
**Important** you have to enable the role manager-script and assign that role to the particular user in tomcat-users.xml file which is in <tomcat_home>/conf/ directory

Follow the Step [1] above ( as being on the same terminal )
```
ex:-> sh 28-pre-scenario-steps.sh
```

Run jmeter scripts in command line (still on the same terminal)
```
ex:-> [path to jmeter]/bin/jmeter -n -t 01-Solution-28-HomeRelam.jmx -p [path to user.properties]/user.properties -l solution28results.jtl
```

Follow the step [2] above. 
```
ex:-> sh 28-post-scenario-steps.sh
```




