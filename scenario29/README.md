# Scenario 29 - Service provider-specific user stores

##### Following scenarios are covered through this automation script.

##### Problem:

- The business users need to access multiple service providers supporting multiple heterogeneous identity federation protocols.
- When the user gets redirected to the identity provider, the users only belong to the user stores specified by the corresponding service provider, should be able to login or get an authentication assertion.
- In other words, each service provider should be able to specify from which user store it accepts users.

##### Scenario:

- Deploy the WSO2 Identity Server as an identity provider over multiple user stores and register all the service providers.
- Extend the pattern 18.0 Fine-grained access control for service providers to enforce user store domain requirement in the corresponding XACML policy.
- Use a regular expression to match allowed user store domain names with the authenticated user’s user store domain name.

_Products: WSO2 Identity Server 5.0.0+_

##### Automated Flow for Asset Creation

- Create a secondary user store
- Create a role and user in secondary userstore
- Create Travelocity Service Provider
- Create a xacml policy and publish to PDP to allow access only to secondary userstore users
- Clear down tests

##### Automated Flow for Positive Path

- Login to travelocity application with a user from seconday userstore allows to login to the web application.

##### Automated Flow for Positive Path

- Login to travelocity application with a user from primary userstore doesn't to login to the web application.

##### Prerequisites

- Create a database in mysql with the name of 'IS_Scenario29_Userstore'
- Source the respective mysql db script found in [IS_HOME]/dbscripts to the created database
- Create a user in secondary userstore as 'admin1' (or any name which configured through user.properties). The reason for having an existing user is when creating a role with admin services, it's necessary to include an existing user.

##### Limitations

Currently there's a limitation with xacml policy publishing as described in [1].

[1] https://wso2.org/jira/browse/IDENTITY-7024


