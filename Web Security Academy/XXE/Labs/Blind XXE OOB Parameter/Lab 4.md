# [Blind XXE](https://portswigger.net/web-security/xxe/blind) with out-of-band interaction via XML parameter entities

In this lab use a [Parameter Entity](https://www.w3.org/TR/xml/#dt-PE) defined below

![[XXE/Labs/Blind XXE OOB Parameter/images/payload.png]]
The interaction is generated as the parameter entity is evaluated without an explicit call within the XML body:

![[XXE/Labs/Blind XXE OOB Parameter/images/exploited.png]]

