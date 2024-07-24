This lab is vulnerable to [DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based) via client-side [prototype pollution](https://portswigger.net/web-security/prototype-pollution). The website's developers have noticed a potential gadget and attempted to patch it. However, you can bypass the measures they've taken.

To solve the lab:

1. Find a source that you can use to add arbitrary properties to the global `Object.prototype`.
    
2. Identify a gadget property that allows you to execute arbitrary JavaScript.
    
3. Combine these to call `alert()`.
    

You can solve this lab manually in your browser, or use [DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader) to help you.

This lab is based on real-world vulnerabilities discovered by PortSwigger Research. For more details, check out [Widespread prototype pollution gadgets](https://portswigger.net/research/widespread-prototype-pollution-gadgets) by [Gareth Heyes](https://portswigger.net/research/gareth-heyes).

[](https://portswigger.net/academy/labs/launch/9f29effeafaa743b0f87d5682f68184437df0b23db7ce32b2377869a95045976?referrer=%2fweb-security%2fprototype-pollution%2fclient-side%2fbrowser-apis%2flab-prototype-pollution-client-side-prototype-pollution-via-browser-apis)
# Solution

1. Look at the application source files to detect the vulnerable portion of the code:

![[Advanced Topics/Prototype pollution/Prototype pollution via browser APIs/labs/Client-side prototype pollution via browser APIs/images/vuln.png]]

2. Find a source to pollute the `Object` prototype

The URL is processed in such a way that is possible to inject arbitrary values on the `value` property of the `Object` prototype:

```
?__proto__[value]=testdata
```

Which is reflected within the application:

![[polluted-chain.png]]

3. The gadget is already in the vulnerable code and it simply places the injected property on a `<script>` element in the DOM:

![[Advanced Topics/Prototype pollution/Prototype pollution via browser APIs/labs/Client-side prototype pollution via browser APIs/images/reflected.png]]

4. Now craft the appropriate payload to solve the lab

```
?__proto__[value]=data:,alert(2)
```

![[Advanced Topics/Prototype pollution/Prototype pollution via browser APIs/labs/Client-side prototype pollution via browser APIs/images/solved.png]]