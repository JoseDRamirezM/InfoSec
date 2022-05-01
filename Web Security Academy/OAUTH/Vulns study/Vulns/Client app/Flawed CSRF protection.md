# Flawed CSRF protection

The `state` parameter on OAuth authorization requests is important as it acts as a <font color=red>
CSRF token</font> for the client application. It must be an unpredictable value. Authorization requests that don't contain this parameter can lead to the following scenarios:

- An attacker initiates an OAuth flow and trick a user to complete it. Similar to a traditional [CSRF attack](https://portswigger.net/web-security/csrf)(making the user perform action they don't intent to). 
- Allows an attacker to hijack the victim user's account on the client application by binding it to their own social media account. If the application allows to link a social media profile as a mean of authentication.