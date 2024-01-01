# Method-based access control can be circumvented
#WRITEUP <hr>

## Recon

This time the application's admin panel has a functionality to elevate the privileges of a given user.

![[adminFunctionality.png]]

The admin panel is in `/admin`

![[enpoint1.png]]

The admin functionality makes a POST request to `/admin-roles` with the following parameters:

![[requestParameter.png]]

## Vulnerability assessment

Test if it is possible to access the `/admin-roles` endpoint with an alternative HTTP method logged in as a normal user.

![[Server-Side Vulnerabilities/AccessControl/labs/Method-based access control can be circumvented/images/PoC.png]]

## Exploitation

Now provide the appropriate parameters having in mind the HTTP method used.

![[AccessControl/labs/Method-based access control can be circumvented/images/exploit.png]]

Now the `wiener` user is an administrator and the lab is solved.