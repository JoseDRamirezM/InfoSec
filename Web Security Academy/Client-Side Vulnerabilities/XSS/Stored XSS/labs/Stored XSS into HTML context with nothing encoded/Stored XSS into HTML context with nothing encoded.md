This lab contains a [stored cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the comment functionality.

To solve this lab, submit a comment that calls the `alert` function when the blog post is viewed.

# Exploitation

Check the comment functionality:

![[Client-Side Vulnerabilities/XSS/Stored XSS/labs/Stored XSS into HTML context with nothing encoded/images/payload.png]]

Submit the comment.