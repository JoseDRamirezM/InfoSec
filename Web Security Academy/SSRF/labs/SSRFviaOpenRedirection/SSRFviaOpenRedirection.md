# SSRFviaOpenRedirection
#WRITEUP <hr>
## Recon

First I had to find the open redirection vulnerability. To do that I looked for a parameter like `path` in the application's functionalities and found it in the following link:

![[vulnLink.png]]

By analyzing the response to any of the items in the listing.

![[open.png]]


## Vulnerability assessment

Try to manipulate the parameter to redirect the page to `https://google.com`



## Exploitation

