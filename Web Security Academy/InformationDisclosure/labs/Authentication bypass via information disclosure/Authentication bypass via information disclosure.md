# Authentication bypass via information disclosure

#WRITEUP 
#INFORMATIONDISCLOSURE 

<hr>

## Recon

The application front-end uses a custom HTTP header that allows to bypass the authentication of the administrative interface. Use the custom header to delete user Carlos.

## Vulnerability assessment

Inspecting the application didn't reveal much, but performing some enumeration will provide the way to bypass the authentication as follows:

1. Identify the `TRACE` method is enabled in the server.
![[trace-active.png]]
`I found this by running the Nikto tool`

I couldn't find another way to know this via enumerating the server apart from nikto and an nmap scan.

2. Identify the admin interface is in the `/admin` endpoint.
3. Try to access the `/admin` endpoint using the `TRACE` HTTP method.


![[trace.png]]

A file will be downloaded which contains the custom header that is appended somehow along the way the request is made to the backend.

![[custom-header.png]]

## Exploitation

Now all I got to do was to put the pieces together this means: request the `/admin` endpoint with the custom header set to a private IP address to comply to be a `local user`.

![[InformationDisclosure/labs/Authentication bypass via information disclosure/images/bypass.png]]

The request returns `200 OK` and I got access to the admin interface. Lastly delete Carlo's account and the lab is solved.



