This lab is vulnerable to routing-based [SSRF](https://portswigger.net/web-security/ssrf) due to its flawed parsing of the request's intended host. You can exploit this to access an insecure intranet admin panel located at an internal IP address.

To solve the lab, access the internal admin panel located in the `192.168.0.0/24` range, then delete the user `carlos`.

# Vuln assessment

Note that the server allows to request the home page by supplying an absolute URL.

![[first-step.png]]

Try changing the Host header while keeping the absolute URL.

![[Advanced Topics/Host Header Attacks/labs/SSRF via flawed request parsing/images/SSRF.png]]

The host is indeed vulnerable to SSRF

# Exploitation

Brute force the IP address to access to the administration panel

![[host-found.png]]

The response redirects to the `admin` path

![[admin-panel-request.png]]

Now delete the target user form the admin panel

![[solve-lab.png]]
After sending this request the lab is solved!