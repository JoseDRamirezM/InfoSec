This lab makes an assumption about the privilege level of the user based on the HTTP Host header.

To solve the lab, access the admin panel and delete the user `carlos`.

# Recon

The application perform a simple check on the Host header.

![[Advanced Topics/Host Header Attacks/labs/Host Header authentication bypass/images/bypass.png]]

![[other-host-value.png]]

Access the panel and delete the target user.

In the request for deletion also change the Host header, otherwise it will not work.

![[delete-user.png]]