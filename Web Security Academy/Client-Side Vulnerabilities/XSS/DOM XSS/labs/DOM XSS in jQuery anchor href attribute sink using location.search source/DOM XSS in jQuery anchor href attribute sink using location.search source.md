This lab contains a [DOM-based cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/dom-based) vulnerability in the submit feedback page. It uses the jQuery library's `$` selector function to find an anchor element, and changes its `href` attribute using data from `location.search`.

To solve this lab, make the "back" link alert `document.cookie`.

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/DOM XSS in jQuery anchor href attribute sink using location.search source/images/jquery.png]]

Inject the query param with `javascript:alert(document.cookie)`

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/DOM XSS in jQuery anchor href attribute sink using location.search source/images/query.png]]