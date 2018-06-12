###Jmeter scripts are available for scenario-06 which explained in blog post[1]

Scripts will be able to run for following accordingly:

1. Script ['01-Scenario-06-Configure-RemoteUerStore-SPandIDP.jmx']

This is to add configurations in Identity Server as below
- Registering Service Provider for web app (e.g. travelocity.com)
- Registering Identidy Providers (e.g. twitter, google - note that this can be extended to add more value sets)
- Register a carbonRemoteUserStoreManager as secondary user store (see prerequisite-1 for more details)


2. Script [02-Soulution-06-ProvisionFederatedUsersToTenant.jmx]

This is to run the solution with federation login using IDPs, and provision the federated user into the remote user store
- Login to travelocity web app
- Consent management 
- Federation login
- JIT provision to remote user store


3. Script [03-Scenario-06-Remove-Userstore-SP-IDP-Users.jmx]

This is to clean up the configured stuffs from the environment

- Remove the SP
- Remove the IDPs
- Remove user store and provisioned user (note here it will be able to remove all users except admin with an "if" check)

####prerequisites

1. To add carbonRemoteUserStore, there should be a carbon server up and running  - in case you should be able to use another IS server with port offset(e.g.9444)
2. Configure a web app using tomcat - in case written script already available to deploy it
3. Check and modify the user.properties file for user & environment variables according to yours.


####how to run

Simply execute the run-scenario.sh from scenario06



[1] https://medium.facilelogin.com/thirty-solution-patterns-with-the-wso2-identity-server-16f9fd0c0389

