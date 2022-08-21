# File path traversal simple case
#DIRECTORYTRAVERSAL 
#WRITEUP 
<hr>

## Recon

The lab consists of an e-commerce website, when visiting any of the products listed the app makes a request to load the corresponding image to a given item.

![[file_name.png]]

## Exploitation

Test a directory traversal payload in the `filename` parameter to retrieve the `/etc/passwd` system file.

![[DirectoryTraversal/labs/images/payload.png]]

The response to this request will contain the content of the system file.

![[passwd_file.png]]
