#OAuth 2.0 Applications

## 1. A stateless OAuth 2.0 proxy for Single Page Applications (SPAs)

* Build the sample SPA from https://github.com/facilelogin/aratuwa/tree/master/oauth2.0-apps/org.wso2.carbon.identity.oauth.spa

* Copy the artifact(amazon.war) created from the above step to [CATALINA_HOME]\webapps

* This sample assumes Apache Tomcat is running on localhost:8080 and WSO2 Identity Server 5.0.0 or 5.1.0 is running on localhost:9443

* If you use different hostnames or ports, change the hostname and the port inside [CATALINA_HOME]\webapps\amazon\index.html and in.html

* Also note that the value **spaName** query parameter in [CATALINA_HOME]\webapps\amazon\index.html it should match the value **sample1**, which we define later in **oauth_proxy.properties**, if you change this value make sure you change both the places.

* Create a service provider in WSO2 Identity Server for the proxy app. Note that this is not for the SPA. Configure OAuth 2.0 as the Inbound Authenticator, with https://localhost:9443/oauth2-proxy/callback as the callback URL. This is pointing to the **oauth2-proxy** app  we are going to deploy in Identity Server later.

* Create a file with the name **oauth_proxy.properties** under IS_HOME\repository\conf

* Add following properties to the file **oauth_proxy.properties**

```javascript
is_server_ep=https://localhost:9443
client_id=6ktdbCJgmQIqlO1tNiHBQoVelkUa
client_secret=cg5Gg8PfwI28NjLRy64pyffcK4Ia
proxy_callback_url=https://localhost:9443/oauth2-proxy/callback
sp_callback_url_mapping.sample1=http://localhost:8080/amazon/in.html
sp_logout_url_mapping.sample1=http://localhost:8080/amazon/index.html
iv=RandomInitVector
secret_key=Bar12345Bar12345
```
* The value of the client_id and the client_secret should be copied from the service provider you created in Identity Server

* The value of the proxy_callback_url should match the callback URL you configured when creating a service provider in Identity Server

* The value of sp_callback_url  and sp_logout_url should point to the amazon web app running in Apache Tomcat

* The properties iv and secret_key are used to encrypt the tokens, set as cookies. The value of iv must be 16 characters long.

* The value of is_server property must point to the Identity Server.

* Build the OAuth 2.0 proxy app from https://github.com/facilelogin/aratuwa/tree/master/oauth2.0-apps/org.wso2.carbon.identity.oauth.proxy and copy target/oauth2-proxy.war to IS_HOME/repository/deployment/server/webapps

* Restart the Identity Server.

* Once everything is done and both Identity Serevr and Apache Tomcat are up and running, you can test this by visiting http://localhost:8080/amazon and clicking on the Login link.

