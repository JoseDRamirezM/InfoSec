# Password reset broken logic
#WRITEUP 
#AUTHENTICATION 
<hr>

## Recon

Interacting with the web app and checking the login page, I saw a `Forgot password` link. I went to the `/forgot-password` page and entered the email of the known user `wiener` (logging in as the user would reveal the email address or checking the email client).

![[Vulnerabilities/labs/other authentication mechanisms/Password reset broken logic/images/login.png]]

Check the email sent in the email client and go to the provided link.

![[reset_email.png]]

Then enter an arbitrary password and intercept the request.

Change the username body parameter from `weiner` to `carlos`

![[change_username.png]]

After forwarding the request, no error is generating which strongly indicates that the `carlos` password was changed instead of the user `weiner`.

Try to log in with the entered password and username `carlos` which is successful, the lab is solved!
