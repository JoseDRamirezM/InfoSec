
This lab is vulnerable to web cache poisoning because it excludes a certain parameter from the cache key. A user regularly visits this site's home page using Chrome.

To solve the lab, poison the cache with a response that executes `alert(1)` in the victim's browser.

1. Identify a cache oracle 

![[Advanced Topics/Web Cache Poisoning/labs/implementation/WCP via unkeyed query parameter/images/cache-oracle.png]]

2. Probe key handling

The whole point of the lab is to find an unkeyed GET parameter, for that I used param miner specifying to Guess GET parameters.

![[Advanced Topics/Web Cache Poisoning/labs/implementation/WCP via unkeyed query parameter/images/param-miner.png]]

3. Find an exploitable gadget

Testing the `utm_content` parameter, I was able to poison the cache:

![[Advanced Topics/Web Cache Poisoning/labs/implementation/WCP via unkeyed query parameter/images/cache-poison.png]]

While the cache is poisoned the user will receive the payload.

