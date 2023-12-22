# Information disclosure on debug page
#WRITEUP 
#INFORMATIONDISCLOSURE 
<hr>

## Vulnerability assessment

Interact with the application looking for some debug page that contains sensitive information.

I ran `dirsearch` to try to expand the attack surface.

![[dirs.png]]

Then I looked at the source code of the page, searched for `debug` and found this:

![[debug.png]]

Then I followed the link.

## Exploitation

![[secret.png]]

Submit the secret value.


