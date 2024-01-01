This lab contains a [DOM-based cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/dom-based) vulnerability in the search query tracking functionality. It uses the JavaScript `document.write` function, which writes data out to the page. The `document.write` function is called with data from `location.search`, which you can control using the website URL.

To solve this lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that calls the `alert` function.

# Vuln assessment

Find the use of the sink `document.write`

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/DOM XSS in document.write sink using source location.search/images/sink.png]]

# Exploitation

Manipulate the syntax to trigger an alert:


![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/DOM XSS in document.write sink using source location.search/images/xss.png]]

The lab is solved!

`"><svg onload=alert(1)>`