# Scenario 09 - User Management upon multi-layer approval

Following scenarios are covered through this automation script.

### Problem:
- All the user management operations must be approved by multiple administrators in the enterprise in a hierarchical manner

### Scenario:
- Create a workflow with multiple steps. In each step specify who should provide the approval.
- Define a workflow engagement for user management operations and associate the above workflow with it.
- When defining the workflow, define the criteria for its execution.

## Scenario Coverage

Following sub scenarios are covered in the automation script

- Scenario 1 - Defining a workflow with multiple layers of approval
- Scenario 2 - Defining a execution criteria for workflow approval

Example : Each new individual who have the 'Employee' role, should be approved by a user with 'Manager' role and 'Director' role to provide access to the company's information system.

## Prerequisite
Execution of the script has dependency with the IS dashbaord, as the workflows are managed through the IS dashbaord. Therefore, if the hostname of the Identity server changed to something other than 'localhost' make sure to create a certificate, where the CN of the certificate should be compatible with the configured server hostname and import the cert to the client truststore.

## Executing the Scenario 

Export input variables in the terminal
**>>export serverHost=<is_host> serverPort=<is_port>**
Ex:
```
>>export serverHost=is.localtest.com serverPort=9454
```
Execute the pre-scenario script
```
ex:-> sh 09-pre-scenario-steps.sh
```

Run jmeter scripts in command line (still on the same terminal)
```
ex:-> [path to jmeter]/bin/jmeter -n -t 01-Scenario-09-MultilayerApproval.jmx -p [path to user.properties]/user.properties -l scenario09results.jtl
```

Execute the post-scenario script
```
ex:-> sh 09-post-scenario-steps.sh
```
**Note** - For the solution 09 there is no initial dependency of 'pre-scenario' and 'post-scenario' scripts, but to maintain the consistency these scripts are introduced in the execution path.



