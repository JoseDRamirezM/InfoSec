# Unprotected admin functionality with unpredictable URL 

#WRITEUP 
#ACCESSCONTROL 
<hr> <br> 
## Recon

Reading the page's source code reveals the admin endpoint

![[adminEndpoint.png]]

## Vulnerability assessment 

Navigate to the admin panel

![[AccessControl/labs/Unprotected admin functionality with unpredictable URL/images/adminPanel.png]]

It can be accessed without authentication.

## Exploitation

Delete carlos account and the lab is solved.