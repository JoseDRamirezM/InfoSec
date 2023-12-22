# User ID controlled by request parameter, with unpredictable user IDs

#WRITEUP
#ACCESSCONTROL 
<hr>

## Recon

This lab has a horizontal privilege escalation vulnerability on the user account page, but identifies users with GUIDs.

To solve the lab, find the GUID for `carlos`, then submit his API key as the solution.

You can log in to your own account using the following credentials: `wiener:peter`

## Vulnerability assessment

The application uses GUID so it's difficult to guess carlos GUID.

![[GUID.png]]

Try to get from elsewhere in the application, for instance the comments in the site's blog entries.

For this step the attack can be a little more elaborated if you decide to use Burp Intruder to navigate the posts searching for a comment from user `carlos` (simply grep the name).

![[AccessControl/labs/User ID controlled by request parameter, with unpredictable user IDs/images/intruder.png]]

Now check any of the the responses and get the desired GUID.

![[targetGUID.png]]

## Exploitation

Enter the obtained GUID, submit carlos API key and the lab is solved.