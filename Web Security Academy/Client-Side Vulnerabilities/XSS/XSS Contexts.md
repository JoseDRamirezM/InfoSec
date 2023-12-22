When testing for [reflected](https://portswigger.net/web-security/cross-site-scripting/reflected) and [stored](https://portswigger.net/web-security/cross-site-scripting/stored) [XSS](https://portswigger.net/web-security/cross-site-scripting), a key task is to identify the XSS context:

- The location within the response where attacker-controllable data appears.
- Any input validation or other processing that is being performed on that data by the application.

Based on these details, you can then select one or more candidate XSS payloads, and test whether they are effective.

When the XSS context is text between HTML tags, you need to introduce some new HTML tags designed to trigger execution of JavaScript.

Some useful ways of executing JavaScript are:


``` html
<script>alert(document.domain)</script>

<img src=1 onerror=alert(1)>
```

