# Remote code execution via polyglot web shell upload 

#WRITEUP <br> <hr> <br> 
## Recon 

Interact with the image upload functionality. The app validates the uploaded file content meaning it will only accept images.

## Vulnerability assessment

The lab gives a hint about a polyglot. Looking into it it may be possible to embed PHP code within an image metadata using exiftool.

```
exiftool -Comment="<?php echo 'secret ' . file_get_contents('/home/carlos/secret') . ' secret'; ?>" image.jpg -o polyglot.php
```

## Exploitation

Upload the generated payload

![[upload.png]]

Then intercept the response for the "avatar image"

![[FileUploadVulnerabilites/labs/Remote code execution via polyglot web shell upload/images/exploit.png]]

It contains the secret between the provided separators, upload the secret and the lab is solved.

