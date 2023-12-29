This lab contains a [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search query tracking functionality where angle brackets are encoded. The reflection occurs inside a JavaScript string. To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the `alert` function.

# Exploitation

The trick is to inject Javascript code without breaking the syntax:

```html
test';alert(1)//
```

![[Client-Side Vulnerabilities/XSS/Reflected XSS/labs/Reflected XSS into a JavaScript string with angle brackets HTML encoded/images/xss.png]]