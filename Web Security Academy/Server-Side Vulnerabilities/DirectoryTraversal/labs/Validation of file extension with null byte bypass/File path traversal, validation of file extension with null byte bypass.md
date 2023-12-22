# File path traversal, validation of file extension with null byte bypass
#DIRECTORYTRAVERSAL 
#WRITEUP 
<hr>

## Recon

E-commerce app with a vulnerable filename parameter when retrieving product images from the server.

## Exploitation

The app expects the `.jpg` file extension, inserting traversal sequences only will not work.

![[fai.png]]

But appending a null byte and the expected file extension does the trick.

![[null_byte.png]]

Lab solved.