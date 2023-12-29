
This lab contains a [stored cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the comment functionality. To solve this lab, submit a comment that calls the `alert` function when the comment author name is clicked.

# Vuln assessment

Check the comment functionality, checking how user input is reflected in the comment section:

![[test-data.png]]

The comment renders as follows:

![[comment.png]]

![[href.png]]

The URL provided by the user is placed in the `href` attribute of an `<a>` element.

# Exploitation

Try to inject the following payload:

`<a href="javascript:alert(1)">`

![[Client-Side Vulnerabilities/XSS/Stored XSS/labs/Stored XSS into anchor href attribute with double quotes HTML-encoded/images/request.png]]

When the user name is clicked the JS code is executed.

![[Client-Side Vulnerabilities/XSS/Stored XSS/labs/Stored XSS into anchor href attribute with double quotes HTML-encoded/images/xss.png]]