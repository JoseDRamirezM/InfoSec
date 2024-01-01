This lab contains a [DOM-based cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/dom-based) vulnerability in the search blog functionality. It uses an `innerHTML` assignment, which changes the HTML contents of a `div` element, using data from `location.search`.

To solve this lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that calls the `alert` function.

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/DOM XSS in innerHTML sink using source location.search/images/sink.png]]

Search for the `searchMessage` element:

![[span.png]]

The attack vector is:

```
12314</span><img src=1 onerror=alert(1)>
```