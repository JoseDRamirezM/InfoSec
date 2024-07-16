
This lab is vulnerable to web cache poisoning due to discrepancies in how the cache and the back-end application handle ambiguous requests. An unsuspecting user regularly visits the site's home page.

To solve the lab, poison the cache so the home page executes `alert(document.cookie)` in the victim's browser.

# Recon

1. Find a cache oracle

The home page acts as a cache oracle

The `Host` header is placed into the response when using duplicate headers. The second one will override the absolute URL of the loaded script.


![[host-header-poison.png]]


The response with the manipulated server is then cached and delivered to users while the cache is alive.

![[Advanced Topics/Host Header Attacks/labs/Host Header authentication bypass/images/poisoned.png]]

# Exploitation

Create the requested file into the exploit server containing: `alert(document.cookie)` to exploit the poisoned cache.

