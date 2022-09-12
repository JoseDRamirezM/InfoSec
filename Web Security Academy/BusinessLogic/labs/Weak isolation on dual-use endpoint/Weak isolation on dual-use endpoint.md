# Weak isolation on dual-use endpoint

#LOGICFLAWS 
#WRITEUP 
<hr>

## Recon

Interact with the application.

It seems that it is possible to provide a new username in the password change functionality (which is odd). So I tried to change `wiener` for `administrator` but an error appeared telling that the current password was incorrect.

![[change-user.png]]

Then I inspected the request it looked like this:

![[vuln-request.png]]

Then I started removing the value and the parameter one at a time.

## Exploitation

After trying some of them I successfully changed the `administator` user password, by removing the `current-password` parameter.

![[BusinessLogic/labs/Weak isolation on dual-use endpoint/images/exploited.png]]

Then log in as the `administrator` user, delete Carlos and the lab is solved.







