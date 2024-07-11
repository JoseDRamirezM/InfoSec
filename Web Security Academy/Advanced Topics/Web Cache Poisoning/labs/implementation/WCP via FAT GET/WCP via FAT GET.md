This lab is vulnerable to [web cache poisoning](https://portswigger.net/web-security/web-cache-poisoning). It accepts `GET` requests that have a body, but does not include the body in the cache key. A user regularly visits this site's home page using Chrome.

To solve the lab, poison the cache with a response that executes `alert(1)` in the victim's browser.

1. Find a cache oracle

Both

- `/`
- `net/js/geolocate.js?callback=setCountryCookie`

Provide a cache oracle

2. Probe key handling

Again the geolocation file reflects the GET parameter passed from the request.

![[reflected-param.png]]

Then having in mind that a FAT GET request must be issued to exploit the vulnerability I started testing some of the request variants to achieve this purpose until I found the right one:

3. Find an exploitable gadget

Basically maintaining the same GET parameter, overriding the request method with a header and poisoning the function call value in the request body I successfully exploited this lab.

![[Advanced Topics/Web Cache Poisoning/labs/implementation/WCP via FAT GET/images/exploited.png]]

When requesting the resource as the front-end does it:

![[poisoned.png]]
