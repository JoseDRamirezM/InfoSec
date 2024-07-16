
This lab contains an XSS vulnerability that is not directly exploitable due to browser URL-encoding.

To solve the lab, take advantage of the cache's normalization process to exploit this vulnerability. Find the XSS vulnerability and inject a payload that will execute `alert(1)` in the victim's browser. Then, deliver the malicious URL to the victim.

# vuln assessment

Find the potential reflected XSS location.

![[random-search.png]]



![[poison.png]]

![[same-key.png]]

![[deliver-to-victim.png]]