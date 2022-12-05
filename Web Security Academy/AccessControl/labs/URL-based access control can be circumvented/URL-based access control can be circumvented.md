# URL-based access control can be circumvented
#WRITEUP <hr>
## Recon

The lab's information gives the path to the exploitation

	This website has an unauthenticated admin panel at `/admin`, but a front-end system has been configured to block external access to that path. However, the back-end application is built on a framework that supports the `X-Original-URL` header.

## Vulnerability assessment

Test requesting `/admin` using the mentioned header.

![[bypass1.png]]

After submitting the request, the admin panel can be accessed.

![[AccessControl/labs/URL-based access control can be circumvented/images/adminPanel.png]]

## Exploitation

Deleting carlos account is not as trivial as in previous labs, this time the same process as before (appending the correct header and URL) still useful but it's important to know how the application makes that request.

![[appRequest.png]]

Modify the request for it to pass the access control.

![[bypass2.png]]

This time the request change as the image above because it has a GET parameter to determine which account is being deleted, after sending the request the account is deleted.

