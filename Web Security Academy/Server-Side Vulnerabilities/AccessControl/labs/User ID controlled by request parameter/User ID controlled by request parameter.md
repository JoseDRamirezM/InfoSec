
#WRITEUP 
#ACCESSCONTROL 
<hr>

## Recon

This lab has a horizontal privilege escalation vulnerability on the user account page.

To solve the lab, obtain the API key for the user `carlos` and submit it as the solution.

You can log in to your own account using the following credentials: `wiener:peter`

## Vulnerability assessment

Log in with the provided user and check the requests that are made.

![[userID.png]]

Tamper the parameter with the target username.

![[tamper.png]]

## Exploitation

Show the response in the browser and note the data of carlos user is now displayed, submit the API key and the lab is solved.

![[AccessControl/labs/User ID controlled by request parameter/images/exploit.png]]