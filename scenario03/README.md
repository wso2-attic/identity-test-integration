# Scenario 3 - Provision Federated Users by the Identity Provider
Following scenarios are covered through this automation script.

##### Problem:
The business users need to login to multiple service providers via multiple identity providers. For example login to Drupal via Facebook or Yahoo! credentials.
Irrespective of the service provider, need to group federated users by the identity provider and store all the user attributes locally. For example, the identity admin should be able to find all the Facebook user or the Yahoo users who have accessed the system (i.e. login to any service provider)

##### Scenario:
  - Deploy WSO2 Identity Server over multiple user stores and name each user store after the name of the corresponding identity provider.
Represent each federated identity provider in Identity Server. For example, represent Facebook as an identity provider in Identity Server.
Enable JIT provisioning for each identity provider, and pick the user store domain to provision users.
##### Covered Automations Positive 
- Create SP Travelocity
- Create IDPs Twitter and Facebook
- Create Different Jdbc Secondary user stores to provision Twitter federated users and Facebook federated users
- JIT provisioning Federated users to different secondary user stores according to the IDP that they use to login to SP Travelocity
- Clear down tests



##### Covered Automations Negative
- Fedrated Users Could not login to SP and cannot provision to user stores when incorrect client APP details are configured 



