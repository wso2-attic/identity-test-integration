# This repository is no longer maintained.
Issue reports and pull requests will not be attended.

# identity-test-integration

### Executing the tests.
Please use the following maven command from the root pom or the individual scenarios to run the tests.
```bash
mvn clean verify --fae
```

### List of Scenarios

| *#*  | *Scenario Description*  |
|---|---|
| 01  | Single Sign On between multiple heterogeneous identity federation protocols |
| 02  | Multiple login options by service provider  |
| 03  | Provision federated users by the identity provider |
| 05  | Multi-factor authentication for WSO2 Identity Server management console  |
| 06  | Provision federated users to a tenant  |
| 09  | User management upon multi-layer approval  |
| 10  | Single Sign On with delegated access control  |
  11  | Identity federation between service providers and identity providers with incompatible identity federation protocols |
| 12  | Claim Mapper with Service Provider Travelocity and Identity Provider Facebook and Google  |
| 13  | Fine-grained access control for APIs |
| 14  | Enforce password reset for expired passwords during the authentication flow  |
| 15  | Federation Proxy  |
| 17  | Single Page Application (SPA) proxy  |
| 18  | Fine-grained access control for service providers  |
| 21  | Enforce users to provide missing required attributes while getting JIT provisioned to the local system  |
| 22  | Access a microservice from a web app protected with SAML 2.0 or OIDC  |
| 23  | Single Sign On between a legacy web app, which cannot change the user interface and service providers, which support standard SSO protocols  |
| 25  | Fine-grained access control for SOAP services |
| 26  | User administration operations from a third-party web app  |
| 27  | Authenticate the users against one user store but fetch user attributes from multiple other sources |
| 28  | Home realm discovery  |
| 29  | Service provider-specific user stores  |
