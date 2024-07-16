# Password brute-force via password change
#AUTHENTICATION 
#WRITEUP 

<hr>

## Recon

### Frontend

Log in with the provided credentials and interact with the password change functionality.

If the current password is entered incorrectly and the new passwords match. The account is locked for a minute.

The thing with this lab is to play with the combination of "right/wrong" or "equal/different" elements in the password change form. Until it is known that providing the correct current password and new passwords that don't match generate a particular error message, that is `New passwords do not match`.

### Request

![[username_param.png]]

The password change request contains the username, which completes the scenario for performing a brute-force attack on any user password.

## Exploitation

Use Burp Intruder to perform requests, this time with `username=carlos`, a string marker for the passwords and mismatching new passwords. Wait for it to finish and look for the message `New passwords do not match` in the responses.

![[Vulnerabilities/labs/other authentication mechanisms/Password brute-force via password change/images/intruder.png]]

Once a response with the message is found it is certain that the user password has been found.

![[Server-Side Vulnerabilities/Authentication/Vulnerabilities/labs/other authentication mechanisms/Password brute-force via password change/images/found.png]]

Log in to `carlos` account and the lab is solved!