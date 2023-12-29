This lab contains a simple [reflected cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the `alert` function.

# Vuln assessment

Test the search bar entry point

![[Client-Side Vulnerabilities/XSS/Reflected XSS/labs/Reflected XSS into HTML context with nothing encoded/images/entry-point.png]]

Anything passed in the parameter is echoed back to the user:

![[Client-Side Vulnerabilities/XSS/Reflected XSS/labs/Reflected XSS into HTML context with nothing encoded/images/reflection-point.png]]

# Exploitation

Try injecting an XSS payload

![[Client-Side Vulnerabilities/XSS/Reflected XSS/labs/Reflected XSS into HTML context with nothing encoded/images/exploit.png]]


Fin
