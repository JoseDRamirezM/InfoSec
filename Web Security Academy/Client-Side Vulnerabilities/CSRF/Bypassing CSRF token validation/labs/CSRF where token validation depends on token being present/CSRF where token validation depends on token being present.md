This lab's email change functionality is vulnerable to CSRF.

To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.

The original request looks like:

![[original-request.png]]

Try to change the email, removing the csrf token from the request:

![[exploit-request.png]]

It works!

# Exploitation 

Generate a PoC with burp, store and deliver it to the victim.