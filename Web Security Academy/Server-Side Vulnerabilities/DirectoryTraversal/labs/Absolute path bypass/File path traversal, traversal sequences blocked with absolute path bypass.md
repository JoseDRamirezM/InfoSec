# File path traversal, traversal sequences blocked with absolute path bypass
#DIRECTORYTRAVERSAL 
#WRITEUP 
<hr>

## Recon

Same scenario as in [[File path traversal simple case]] this time the vulnerable parameter is protected against traversal sequences. The same requests are issued to retrieve the image of each product.

## Exploitation

As the lab suggests use an absolute path to the `/etc/passwd` system file, in the vulnerable parameter.

![[absolute_path.png]]

Lab solved.



