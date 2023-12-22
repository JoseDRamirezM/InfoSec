# Password reset poisoning via middleware
#AUTHENTICATION 
#WRITEUP 
<hr>

## Recon

Log in with the provided user credentials and try to figure out a way to get the reset password token of user `carlos`.

Try to reset the password of the provided user to check how the functionality works.

## Exploit background

According to the information [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Host) the `X-Forwarded-Host` header helps to determine the original host that the client requested, when there's a reverse proxy scenario. Which makes the host names and ports differ from the origin server handling the request.

With that in mind, in this case it is possible to trick the server into sending the request that contains the secret token necessary for the password reset, to a attacker controlled site.

## Exploit
First go through the password reset flow and intercept the request to the page that ask for the user email/username.

![[flow.png]]

In that request, inject the `X-Forwarded-Host` header with the provided exploit server domain name.

![[req_1.png]]

Forward the request and check the exploit server access log.

![[token.png]]

A request containing the reset password token for user `carlos` is present. I assume the previous `POST` request generates the `GET` request to handle sending the email to the user with the correct URL.

 Go back to the provided user email client and go to the provided URL for the password reset but edit the token to the one received in the exploit server. Complete the password reset, and log in as user `carlos`.

![[path.png]]