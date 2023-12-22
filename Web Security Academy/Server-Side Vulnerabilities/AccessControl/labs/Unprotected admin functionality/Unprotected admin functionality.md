# Unprotected admin functionality <br>#WRITEUP <br> <hr> <br> 
## Recon

Basic recon will lead to the `robots.txt` file which includes the admin panel endpoint.

![[AccessControl/labs/Unprotected admin functionality/images/robots.png]]

## Vulnerability assessment

The admin panel is accessed without any authentication.

![[AccessControl/labs/Unprotected admin functionality/images/adminPanel.png]]

## Exploitation

Delete carlos account and the lab is solved.