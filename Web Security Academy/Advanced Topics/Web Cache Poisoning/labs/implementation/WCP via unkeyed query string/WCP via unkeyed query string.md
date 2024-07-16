This lab is vulnerable to web cache poisoning because the query string is unkeyed. A user regularly visits this site's home page using Chrome.

To solve the lab, poison the home page with a response that executes `alert(1)` in the victim's browser.



1. Identify a cache oracle 

Request to any of the blog posts will reveal cache information:

![[Advanced Topics/Web Cache Poisoning/labs/implementation/WCP via unkeyed query string/images/cache-oracle.png]]

![[cache-oracle-1.png]]

2. Probe key handling

The query string parameters were reflected on the response, making it possible to manipulate the page content:

![[reflected-query-param.png]]

3.  Find an exploitable gadget

From here was just a matter of getting the right payload to execute the javascript action and poison the cache to deliver the attack.

![[last-try.png]]

Once the cache is poisoned it will be delivered to all users that visit the homepage:

![[cached-response.png]]