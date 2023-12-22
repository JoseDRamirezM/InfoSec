# Remote code execution via web shell upload

#FILEUPLOAD 
#WRITEUP 

<hr>

## Recon

This lab contains a vulnerable image upload function. It doesn't perform any validation on the files users upload before storing them on the server's filesystem.

To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file `/home/carlos/secret`. Submit this secret using the button provided in the lab banner.

You can log in to your own account using the following credentials: `wiener:peter`

## Vulnerability assessment

Identify the entry point and upload the webshell pointing to the given path.

![[Server-Side Vulnerabilities/FileUploadVulnerabilites/labs/Remote code execution via web shell upload/images/entry-point.png]]

The avatar image upload may be a potential entry point, craft the webshell and try to upload it.

![[success-and-file-path.png]]

It succeeds.


## Exploitation

Inspect the saved avatar in the account page and then visit the file path where the avatar was saved to trigger the execution.

![[file-path.png]]

The path will reveal the secret and the lab is solved.

![[FileUploadVulnerabilites/labs/Remote code execution via web shell upload/images/secret.png]]