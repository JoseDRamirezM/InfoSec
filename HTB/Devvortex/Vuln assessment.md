# Port 22 (SSH)

OpenSSH 8.2p1 Ubuntu 4ubuntu0.9
# Port 80 (HTTP)

nginx 1.18.0 (Ubuntu)

## Web server enumeration
## devvortex.htb

Not much to see here...

## dev.devvortex.htb

- Navigating to `/administrator` I found a joomla login:

![[joomla-login.png]]

I tried to brute force the login but it was useless

- Checking the `/api` endpoint with the `scanner/http/joomla_api_improper_access_checks` metasploit module I was able to retrieve the super user username and password:

![[username-password.png]]


[[Exploitation]]