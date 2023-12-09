This lab controls access to certain admin functionality based on the Referer header. You can familiarize yourself with the admin panel by logging in using the credentials `administrator:admin`.

To solve the lab, log in using the credentials `wiener:peter` and exploit the flawed [access controls](https://portswigger.net/web-security/access-control) to promote yourself to become an administrator.

# Recon

Test the admin panel functionality

![[AccessControl/labs/Referer-based access control/images/admin-panel.png]]

The resulting request is:

![[admin-upgrade.png]]

Try to remove the `Referer` header

![[admin-401.png]]

# Exploitation

Log in as `wiener` and use the same request from the previous tests, changing the session cookie and the `username` GET parameter:

![[AccessControl/labs/Referer-based access control/images/exploit.png]]

Now `wiener` is an admin user.

