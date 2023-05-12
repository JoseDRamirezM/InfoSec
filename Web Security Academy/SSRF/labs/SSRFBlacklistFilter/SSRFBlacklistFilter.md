# SSRFBlacklistFilter
#WRITEUP <hr>
## Recon

The stock check functionality is vulnerable to SSRF.

## Vulnerability assessment

Try to bypass filters to access the admin interface. The following payload grants access:

`http://127.1/ADMIN`

![[SSRF/labs/SSRFBlacklistFilter/images/payload.png]]

## Exploitation

Delete user carlos

![[SSRF/labs/SSRFBlacklistFilter/images/exploit.png]]

