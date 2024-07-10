This lab is vulnerable to [web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning) because it excludes a certain parameter from the cache key. There is also inconsistent parameter parsing between the cache and the back-end. A user regularly visits this site's home page using Chrome.

To solve the lab, use the parameter cloaking technique to poison the cache with a response that executes `alert(1)` in the victim's browser.

1. Identify a cache oracle

The home page provides an oracle

![[oracle.png]]

2.  Probe key handling

Use param miner to guess GET parameters. It TAKES A WHILE

![[Advanced Topics/Web Cache Poisoning/labs/implementation/WCP Parameter Cloaking/images/param-miner.png]]

3. Find an exploitable gadget

