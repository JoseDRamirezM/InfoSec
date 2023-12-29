
This lab contains a [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search blog functionality where angle brackets are HTML-encoded. To solve this lab, perform a cross-site scripting attack that injects an attribute and calls the `alert` function.

# Vuln assessment

The app places user input as the `value` attribute of an `<input>` element within the DOM:

![[Client-Side Vulnerabilities/XSS/Reflected XSS/labs/Reflected XSS into attribute with angle brackets HTML-encoded/images/reflection-point.png]]

# Exploitation

Try to inject attributes to the element, resulting in the following payload:

```html
testing" autofocus onfocus=alert(1) x="
```