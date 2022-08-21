# File path traversal, validation of start of path
#DIRECTORYTRAVERSAL 
#WRITEUP 
<hr>

## Recon

E-commerce app with a vulnerable filename parameter when retrieving product images from the server.

## Exploitation

As the lab suggest provide the expected base folder and use the suiting traversal sequences to the root folder, then retrieve the `/etc/passwd` system file.

![[base_folder.png]]

Lab solved.