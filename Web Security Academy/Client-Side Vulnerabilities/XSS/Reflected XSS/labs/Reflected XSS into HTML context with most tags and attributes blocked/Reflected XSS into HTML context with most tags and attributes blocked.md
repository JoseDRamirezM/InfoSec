# Vuln assessment

When trying to inject HTML tags the WAF blocks them:

![[tag-blocked.png]]

Using the [XSS Cheatsheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)enumerate specifically which tags are blocked using an Intruder Attack:

![[Client-Side Vulnerabilities/XSS/Reflected XSS/labs/Reflected XSS into HTML context with most tags and attributes blocked/images/tags.png]]

Filter the requests that contains the message from the WAF

![[available-tags.png]]

# Exploitation

Use I got to use the body tag to execute JavaScript code, which is only possible by using an attribute:

![[attributes-blocked.png]]

Do the same thing as before, but this time enumerate which events/attributes are allowed:

![[allowed-events.png]]

Use the `onresize` event and to trigger it, use the exploit server to craft an `iframe` which will load the page with the reflected XSS payload and which will be resized once the page is loaded to trigger the event:

```HTML
<iframe src="https://0af4000b03a8d3a280cfee0d00050003.web-security-academy.net/?search=<body+onresize%3d'print()'></body>" onload=this.style.width='100px'>
```

Once I checked the payload page it worked!

![[Client-Side Vulnerabilities/XSS/Reflected XSS/labs/Reflected XSS into HTML context with most tags and attributes blocked/images/exploit.png]]





