This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't integrated into the site's session handling system.

To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.


CSRF tokens in this lab are single use but they're not "assigned" to a single session. With this behavior its possible to reload the page of the test users to obtain fresh tokens and include them in the exploit delivered to the victim.

1. Obtain a fresh csrf token from either account
2. Generate a CSRF PoC with burp and change the token value
3. Store and deliver to the victim

