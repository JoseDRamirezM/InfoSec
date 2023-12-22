Exploiting [XXE](https://portswigger.net/web-security/xxe) using external entities to retrieve files

Navigate to a product and click the following button:

![[stockFunct.png]]


Intercept the request with Burp and inject the XXE payload:

![[XXE/Labs/ExternalEntities/images/exploited.png]]

The `/etc/passwd` file is retrieved.

