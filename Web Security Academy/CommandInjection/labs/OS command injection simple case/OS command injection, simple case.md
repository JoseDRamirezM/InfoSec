# OS command injection, simple case
#COMMANDINJECTION 
#WRITEUP 
<hr>

## Recon

The lab contains an e-commerce app in which the stock for each product in a specific location can be consulted, the functionality triggers a request that is handled insecurely.

![[CommandInjection/labs/OS command injection simple case/images/recon.png]]

## Exploitation

Try to inject the `whoami` OS command using the parameters from the previous request.

For this lab its easier to inject the `storeId` parameter with the following payload (URL encoded):

`&whoami` 

![[CommandInjection/labs/OS command injection simple case/images/success.png]]

This will trigger the shell program and execute another command:

```shell
funct.sh 1 & whoami
```

The current server user is obtained.

Lab solved.