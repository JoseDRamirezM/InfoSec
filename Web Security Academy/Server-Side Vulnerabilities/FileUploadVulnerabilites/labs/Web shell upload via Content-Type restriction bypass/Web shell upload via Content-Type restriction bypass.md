# Web shell upload via Content-Type restriction bypass 

#FILEUPLOAD 
#WRITEUP  
<hr> 

## Recon 

This lab contains a vulnerable image upload function. It attempts to prevent users from uploading unexpected file types, but relies on checking user-controllable input to verify this.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: `wiener:peter`

## Vulnerability assessment 

Identify the entry point and upload the webshell pointing to the given path bypassing the flawed protection.

Log in and check the `/my-account` page and try to upload the webshell to read the given path.

When submitting the form, check its content with Burp proxy.

![[multipart.png]]

If I send it as it is, it will trigger an error.

![[fail.png]]

That error is telling me exactly what to do...

Change the `Content-Type` header with the `image/png` MIME type.

![[chenge-cont-type.png]]

When I forward the request it succeeds.

![[saved.png]]

## Exploitation

Inspect the `/my-account` page looking for the path on the server where the file was saved.

![[FileUploadVulnerabilites/labs/Web shell upload via Content-Type restriction bypass/images/path.png]]

Visit the path, it will reveal the secret and the submit it.