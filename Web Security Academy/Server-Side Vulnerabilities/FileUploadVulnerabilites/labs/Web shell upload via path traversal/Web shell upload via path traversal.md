# Web shell upload via path traversal  

#FILEUPLOAD 
#WRITEUP  
<hr>  

## Recon  

This lab contains a vulnerable image upload function. The server is configured to prevent execution of user-supplied files, but this restriction can be bypassed by exploiting a [secondary vulnerability](https://portswigger.net/web-security/file-path-traversal).

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: `wiener:peter`

## Vulnerability assessment  

Identify the entry point and upload the webshell pointing to the given path bypassing the flawed protection.

Log in and check the `/my-account` page and try to upload the webshell to read the given path.

When submitting the form, check its content with Burp proxy.

![[multipart.png]]

It will save the file

![[saved.png]]

Go to the path and notice that the server is just returning the file contents in plain text instead of executing the PHP code.

![[plain.png]]

Repeat the process above but specify the `filename` parameter of the `multi-part` form to  `../exploit.php`. That will save the file one folder above in the structure, which probably won't have such strict controls.

![[traversal.png]]

Now visit `/files/exploit.php` and it didn't work. I started checking the response to the form request and noticed the server was stripping the traversal sequences before passing the filename to the code that handles this functionality.

![[not-working.png]]

So I tried applying some bypass techniques until I knew I got to URL encode the traversal sequences.

## Exploitation

Repeat the last steps of the process above URL encoding the traversal sequences to effectively store the webshell in another directory.

![[working.png]]

Now visit `/files/exploit.php` and it should retrieve the secret. To complete the lab submit it.

