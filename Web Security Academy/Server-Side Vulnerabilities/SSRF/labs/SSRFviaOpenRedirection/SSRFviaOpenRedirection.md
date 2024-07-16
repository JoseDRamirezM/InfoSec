# SSRFviaOpenRedirection
#WRITEUP <hr>
## Recon

First I had to find the open redirection vulnerability. To do that I looked for a parameter like `path` in the application's functionalities and found it in the following link:

![[vulnLink.png]]

Clicking the`Next product` link, the following request is issued:

![[open.png]]

## Vulnerability assessment

Test the `path` parameter for open redirection:

![[redirection.png]]

The open redirection is confirmed

The hard part is to find the appropriate parameter to place the payload, looking at the stock check functionality it uses the `/product/XXX` path, hence it is possible to feed the vulnerable URL to generate an open redirection to the admin panel, directly from the api:

Vulnerable URL (Open redirection):

```
https://0ae0007503e530e180dbda9700a900ea.web-security-academy.net/product/nextProduct?path=http://192.168.0.12:8080/admin
```
``
Payload for the stock check functionality (URL encode it):

```
/product/nextProduct?path=http://192.168.0.12:8080/admin
```

![[Server-Side Vulnerabilities/SSRF/labs/BlindSSRF-OOB/images/SSRF.png]]

Now we hace access to the admin interface.

## Exploitation

Delete user carlos to complete the lab:

![[SSRF/labs/BlindSSRF-OOB/images/exploited.png]]

