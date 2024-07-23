This lab is vulnerable to DOM XSS via client-side prototype pollution. This is due to a gadget in a third-party library, which is easy to miss due to the minified source code. Although it's technically possible to solve this lab manually, we recommend using [DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/prototype-pollution) as this will save you a considerable amount of time and effort.

To solve the lab:

1. Use DOM Invader to identify a prototype pollution and a gadget for DOM XSS.
    
2. Use the provided exploit server to deliver a payload to the victim that calls `alert(document.cookie)` in their browser.
    

This lab is based on real-world vulnerabilities discovered by PortSwigger Research. For more details, check out [Widespread prototype pollution gadgets](https://portswigger.net/research/widespread-prototype-pollution-gadgets) by [Gareth Heyes](https://portswigger.net/research/gareth-heyes).

# Solution

Using the DOM Invader will quickly detect the vulnerability:

![[Advanced Topics/Prototype pollution/Client-Side Prototype Pollution/labs/Client-side prototype pollution in third-party libraries/images/dom-invader.png]]

From here just change the payload to:

```
alert(document.cookie)
```

And deliver the exploit

![[Advanced Topics/Prototype pollution/Client-Side Prototype Pollution/labs/Client-side prototype pollution in third-party libraries/images/solved.png]]