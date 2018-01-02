# Solution 14 - Enforce password reset for expired passwords during the authentication flow
Note that Solution 2 was used to test the scenario

### Problem:
- During the authentication flow, enforce to check whether the end-user password is expired and if so, prompt the user to change the password.

### Solution 1
- Configure multi-step authentication for the corresponding service provider.
- Engage basic authenticator for the first step, which accepts username/password from the end-user.
- Write a handler (a local authenticator) and engage it in the second step, which will check the validity of the user’s password and if it is expired then prompt the user to reset the password or use the 
- Sample implementation: http://blog.facilelogin.com/2016/02/enforce-password-reset-for-expired.html
- Products: WSO2 Identity Server 5.0.0+

### Solution 2
- Follow the guide provided in the [connector doc](https://docs.wso2.com/display/ISCONNECTORS/Configuring+Password+Policy+Authenticator) 

## Scenario Coverage

Following sections are covered from the automation script

- 1 - Create a user and a role

- 2 - Create a claim to store last password changed time

- 3 - Create and configure to force password reset in authentication flow

- 4 - Scenario 01 User who logs in to the system first time will be prompted to reset the password and then login to the application

- 5 - Scenario 02 User who reseted the password will not be allowed to login to the application with the previos password

- 6 - Scenario 03 User who reseted the password is now able to login to the app with the new password






