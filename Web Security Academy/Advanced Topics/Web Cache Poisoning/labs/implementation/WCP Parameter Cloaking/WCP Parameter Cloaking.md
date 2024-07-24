This lab is vulnerable to [web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning) because it excludes a certain parameter from the cache key. There is also inconsistent parameter parsing between the cache and the back-end. A user regularly visits this site's home page using Chrome.

To solve the lab, use the parameter cloaking technique to poison the cache with a response that executes `alert(1)` in the victim's browser.

1. Identify a cache oracle

The home page provides an oracle

![[oracle.png]]

The home page didn't have any exploitable behavior.

Look for an imported `.js` file that contains a GET parameter:

![[home-geolocate.png]]

2.  Probe key handling

Use param miner to guess GET parameters or directly perform a parameter cloaking scan. It TAKES A WHILE

![[confusing.png]]

Param miner gives a very confusing result, any extra parameters included into the request will not poison the cache.

Basically the `callback` parameter controls which function is called dynamically in the `.js` file:

![[Advanced Topics/Web Cache Poisoning/labs/implementation/WCP via unkeyed query string/images/reflected.png]]

Leveraging this behavior it's possible to construct a payload that will include an injected function into the file that later will be executed by the front end. This is done by exploiting parameter cloaking or pollution.

```
/js/geolocate.js?callback=setCountryCookie&utm_content=test;callback=alert(1)
```

3. Find an exploitable gadget

The idea is that when the page requests:

```
/js/geolocate.js?callback=setCountryCookie
```

The poisoned version of the file is delivered to the user

![[desired-response.png]]

![[Advanced Topics/Web Cache Poisoning/labs/implementation/WCP Parameter Cloaking/images/cache-poison.png]]

Once the cache is poisoned the lab is solved.