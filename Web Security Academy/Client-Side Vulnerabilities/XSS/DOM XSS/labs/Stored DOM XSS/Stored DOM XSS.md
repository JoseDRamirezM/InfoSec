This lab demonstrates a stored DOM vulnerability in the blog comment functionality. To solve this lab, exploit this vulnerability to call the `alert()` function.

# Vuln assessment

In this lab code review is important:

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/Stored DOM XSS/images/code.png]]

The highlighted code causes the vulnerability:

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/Stored DOM XSS/images/poc.png]]

Using the `replace` function in a filter will only affect the first occurrences of the unwanted characters.

# Exploitation

The `comment.author` attribute is vulnerable, inject an XSS payload in the name parameter of the comments request:

```
Test+name</p><img+src%3d1+onerror%3dalert(1)>
```
