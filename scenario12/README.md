#Scenario 12  Claim mapper

####Problem:

The claim dialect used by the service provider is not compatible with the default claim dialect used by the WSO2 Identity Server.
The claim dialect used by the federated (external) identity provider is not compatible with the default claim dialect used by the WSO2 Identity Server.

####Scenario:

Represent all the service providers in the WSO2 Identity Server and configure the corresponding inbound authenticators (SAML, OpenID, OIDC, WS-Federation).
For each service provider define custom claims and map them to the WSO2 default claim dialect.
Represent all the identity providers in the WSO2 Identity Server and configure corresponding federated authenticators (SAML, OpenID, OIDC, WS-Federation).
For each identity provider define custom claims and map them to the WSO2 default claim dialect.

####Products:
WSO2 Identity Server 5.5.0

####Configurations

All the configurations and pre-requisites have been automated using run-scenarios.sh which is in the root directory of the scenario12


