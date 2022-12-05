# User role controlled by request parameter

#WRITEUP <hr>

## Recon

The lab gives a hint about a forgeable cookie, then inspect the login process searching for this.

![[forgeableCookie.png]]

The possible attack vector is found.

## Vulnerability assessment

Change the value from `false` to `true` in the `Admin` cookie.

![[tamperCookie.png]]

Then try to access the `/admin` page

![[accessAdminPanel.png]]

It works!

![[AccessControl/labs/User role controlled by request parameter/images/adminPanel.png]]

## Exploitation

Delete carlos account and the lab is solved.



