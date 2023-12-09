
This lab has an admin panel with a flawed multi-step process for changing a user's role. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.

To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed [access controls](https://portswigger.net/web-security/access-control) to promote yourself to become an administrator.

# Recon

The admin panel:

![[admin-panel.png]]

This process involves two requests:
1. Initial click on upgrade/downgrade user
2. Confirmation dialog

![[confirmation.png]]

# Exploitation

Try to use the less privileged user session cookie to request the second step request which looks like:

![[second-step.png]]

Make the changes:

![[AccessControl/labs/Multi-step process with no access control on one step/images/exploit.png]]

Now wiener is an administrator:

![[AccessControl/labs/Multi-step process with no access control on one step/images/solved.png]]

