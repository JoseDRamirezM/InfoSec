# Web shell upload via extension blacklist bypass 

#FILEUPLOAD 
#WRITEUP 

<hr><br>
## Recon 

This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed due to a fundamental flaw in the configuration of this blacklist.

To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: `wiener:peter`

## Vulnerability assessment <br>
Identify the entry point and upload the webshell pointing to the given path bypassing the flawed protection.

Log in and check the `/my-account` page and try to upload the webshell to read the given path.

Submitting the form as it is, will trigger an error.

![[FileUploadVulnerabilites/labs/Web shell upload via extension blacklist bypass/images/fail.png]]

From the response I know the target is an Apache server. 

## Exploitation

One thing to try is to overwrite/create the `.htaccess` file of the folder where the avatar is saved to map an arbitrary extension to execute as `php` code.

![[new-extension.png]]

Here I mapped the `.evil` extension to execute as `php` code in the `avatars` directory and the server didn't generate any error. 

Next try to upload the webshell but with `.evil` extension, when I visited the path `/files/avatars/exploit.evil` I found the secret.

To complete the lab submit the secret value.
