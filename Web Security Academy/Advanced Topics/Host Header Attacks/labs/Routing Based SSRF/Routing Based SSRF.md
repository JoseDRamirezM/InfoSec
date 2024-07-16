
This lab is vulnerable to routing-based [SSRF](https://portswigger.net/web-security/ssrf) via the Host header. You can exploit this to access an insecure intranet admin panel located on an internal IP address.

To solve the lab, access the internal admin panel located in the `192.168.0.0/24` range, then delete the user `carlos`.

# Recon

Test the host header injecting a collaborator endpoint to see what happens:

![[Advanced Topics/Host Header Attacks/labs/Routing Based SSRF/images/ssrf.png]]

This is clearly vulnerable to SSRF.

# Vuln assessment

Brute force the private host range using Burp Intruder:

![[Advanced Topics/Host Header Attacks/labs/Routing Based SSRF/images/found.png]]

Be sure to disable this option

![[disable.png]]

The page redirects to `/admin`

![[delete user.png]]