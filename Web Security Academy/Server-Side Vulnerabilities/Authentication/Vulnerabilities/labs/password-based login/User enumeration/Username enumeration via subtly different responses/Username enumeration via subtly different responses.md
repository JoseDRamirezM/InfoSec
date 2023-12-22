# Username enumeration via subtly different responses
#AUTHENTICATION 
#WRITEUP 

1. Enumerate the user

Use Burp's `Intruder` to craft the appropriate attack.

After all the payloads have been tested I checked the responses but there was no obvious differences.

I applied a filter but at first it didn't work because (I was lazy to put the dot, but that worked) it matched all requests. But then I tried to put literally the message on the page.


![[filter.png]]

![[valid_user.png]]

![[subtle.png]]

This time it was harder to find the response difference. It was very subtle indeed, a dot.

2. Dictionary attack on the password

Knowing the user is `archie` guess the password using Burp's `Intruder`

The password is easily found looking at the response status code.

![[Authentication/Vulnerabilities/labs/password-based login/User enumeration/Username enumeration via subtly different responses/images/password.png]]

Log in and the lab is solved.