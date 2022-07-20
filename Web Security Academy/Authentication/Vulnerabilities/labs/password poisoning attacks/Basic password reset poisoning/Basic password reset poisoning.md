# Basic password reset poisoning

## Recon

There's a password reset functionality. Explore it with the provided user.

When the form with the username/email is submitted an email is received containing a password reset link

## Exploitation

Then inject the host header with the exploit server domain name

![[host_header.png]]

Next check the server's access log where the password reset token will be found.

![[exploit_server.png]]

Then go to the original URL replacing the obtained token and reset `carlos` password.

![[pass_change.png]]

Finally log in as `carlos`.

