# User role can be modified in user profile
#WRITEUP 
<hr>

## Recon

The lab reads "This lab has an admin panel at `/admin`. It's only accessible to logged-in users with a `roleid` of 2". So explore the application searching for a way to modify this attribute from the user.

The most promising vulnerable functionality was the one to change the user email.

![[promising.png]]


## Vulnerability assessment

The functionality to change the user's email address uses a JSON object within the request, which I modified according to the hints.

![[AccessControl/labs/User role can be modified in user profile/images/exploit.png]]

After submitting this request the interface clearly changed, indicating I elevated my privileges

![[adminConfirmed.png]]

## Exploitation

Access the admin panel and delete carlos account.
