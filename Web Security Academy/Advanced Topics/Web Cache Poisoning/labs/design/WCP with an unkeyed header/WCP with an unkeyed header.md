This lab is vulnerable to web cache poisoning because it handles input from an unkeyed header in an unsafe way. An unsuspecting user regularly visits the site's home page. To solve this lab, poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser.

# Recon

Use the request sent when inspecting a product, to set up the param miner extension and select the functions:

- Header poison
- Unkeyed param



![[param-miner-hit.png]]

The result shows that `X-Forwarded-Host` header is used to generate a dynamic `<script>` HTML element to fetch resources. Inject the header with the appropriate payload to perform the desired action.

![[Advanced Topics/Web Cache Poisoning/labs/design/WCP with an unkeyed header/images/lab-solved.png]]

In the end it was a matter of achieving the XSS attack

```
X-Forwarded-Host: wsseedg2md108fx5bp1f2as1eskj89wy"></script><script>alert(document.cookie)</script>.oastify.com
```
