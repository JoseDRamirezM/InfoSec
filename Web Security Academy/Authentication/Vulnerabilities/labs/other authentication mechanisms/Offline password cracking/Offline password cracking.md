# Offline password cracking
<hr>

## Recon

Login as user `weiner` to check the stay logged in cookie structure.

![[Vulnerabilities/labs/other authentication mechanisms/Offline password cracking/images/cookie.png]]

Decode the cookie.

![[decoded_cookie.png]]

The stay logged in cookie structure is:

`base64(user:md5(password))`

## Steal the cookie

### Find the XSS vulnerability

I tested the comment section of a post in the blog for storesd XSS, by injecting a simple XSS payload in the page.

Payload:

`<script>alert(1)</script>`

I posted the comment and came back to the blog page and the app is vulnerable to stored XSS.

![[stored_XSS.png]]

### Exploit the XSS vulnerability to get the other user cookie

Check the current cookies via the browser's console.

![[console.png]]

Craft a JavaScript payload that allows to steal the other user's cookie.

![[Vulnerabilities/labs/other authentication mechanisms/Offline password cracking/images/payload.png]]

Check the exploit server access log and note that there's an IP address from a private network that returns the session cookies.

![[access_log.png]]

Then extract the cookie and check the content.

![[decoded_carlos_cookie.png]]

Try to decrypt the hash using online tools.

![[carlos_password.png]]

The `carlos` user password is obtained successfully.

Then log in as `carlos` and delete his account.
