This lab contains a [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search blog functionality. The reflection occurs inside a template string with angle brackets, single, and double quotes HTML encoded, and backticks escaped. To solve this lab, perform a cross-site scripting attack that calls the `alert` function inside the template string.


The reflection point is in a string literal:

![[Client-Side Vulnerabilities/XSS/Stored XSS/labs/Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped/images/reflection.png]]


By simply searching for `${alert(1)}` the lab is solved!