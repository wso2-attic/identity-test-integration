# Scenario 01 - Single Sign On between multiple heterogeneous identity federation protocols

## SOLUTION DESCRIPTION

### Problem:

- The business users need to access multiple service providers supporting multiple heterogeneous identity federation protocols.

- Some service providers are on-premise while others are in the cloud. For example Google Apps (SAML 2.0), Salesforce (SAML 2.0), Office 365 (WS-Federation) are cloud based while JIRA, Drupal, Redmine are on-premise service providers.

- A user logs into any of the service providers should be automatically logged into the rest.

### Scenario:

- Deploy WSO2 Identity Server over the enterprise user store.

- Represent each service provider in the WSO2 Identity Server and configure the corresponding inbound authenticators (SAML, OpenID, OIDC, WS-Federation).

- In each service provider, configure WSO2 Identity Server as a trusted identity provider. For example in Google Apps, add WSO2 Identity Server as a trusted identity provider.

Products: WSO2 Identity Server 5.0.0+

### Prerequisites

User needs to deploy travelocity and playground webapps in tomcat server.Check [1] on how to build webapps from repository.

### Configurations

1. Go to scenario01/src/test/resources/user.properties file and change the values of configurations as below.

#### IS Server
serverHost=< HOST NAME OF IS SERVER > <br />
serverPort=< PORT OF THE IS SERVER > <br />
scenarioName=< Scenario Name > <br />

#### User Management
adminusername=< ADMIN USER NAME > <br />
adminpassword=< ADMIN PASSWORD > <br />
adminCredentials=< BASE64 Encoded ADMIN USERNAME:ADMIN PASSWORD > <br />
rolename= < NEW ADMIN ROLE NAME > <br />
usernamePrefix=< NEW ADMIN USERNAME > <br />
noOfUsers= < NUMBER OF USERS TO CREATE > <br />
noUsername=< NEW NON EXISTING USER'S USERNAME > <br />
noPassword=< NEW NON EXISTING USER'S PASSWORD > <br />
permission=< PERMISSION FOR ADMIN ROLE > <br />


#### SP
spname=< SP NAME > <br />
spdescription=< SP DESCRIPTION > <br />
carbonServer=< ISSUER NAME > <br />

## Travelocity

travelocityAppName=travelocity.com
spName=< SP NAME OF TRAVELOCITY > <br />
spDescription=< SP DESCRIPTION OF TRAVELOCITY > <br />

## Playground

playgroundHost=< HOST NAME FOR PLAYGROUND APP > <br />
spName2=< SP NAME OF PLAYGROUND > <br />
spDescription2=< SP DESCRIPTION OF PLAYGROUND > <br />

## Tomcat

tomcatHost=< HOST NAME OF TOMCAT SERVER > <br />
tomcatPort=< PORT OF THE TOMCAT SERVER > <br />


### How to Run

To try out the scenario 01, run the below command.

```bash
mvn clean verify --fae
```

[1] https://docs.wso2.com/display/IS541/Downloading+a+Sample
