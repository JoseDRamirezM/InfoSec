This lab is vulnerable to web cache poisoning because cookies aren't included in the cache key. An unsuspecting user regularly visits the site's home page. To solve this lab, poison the cache with a response that executes `alert(1)` in the visitor's browser.

# Recon

Capture the request for the home page and pass it to param miner to find out the vulnerable cookie:

![[Advanced Topics/Web Cache Poisoning/labs/WCP with unkeyed cookie/images/cookie.png]]


The extension wasn't necessary, manipulate the cookie to check what can be done.

# Exploitation

![[Advanced Topics/Web Cache Poisoning/labs/WCP with unkeyed cookie/images/solved.png]]