# Inconsistent security controls
#LOGICFLAWS 
#WRITEUP 
<hr>

## Recon

The lab objective is to access administrative functionality with an arbitrary user.

Interacting with the application it's necessary to register a new user to access the application. Then I noticed this in the `/my-account` endpoint.

![[change_email.png]]

Then I tried to change the email to a corporate one i.e test@dontwannacry.com

After that I got access to administrative functionality.

![[admin.png]]

Delete user Carlos and the lab is solved.
