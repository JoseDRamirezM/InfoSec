This lab has a simple [reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected) vulnerability. The site is blocking common tags but misses some SVG tags and events.

To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that calls the `alert()` function.

# Vuln assessment

The app reflects the `<svg>` input:

![[svg_tag.png]]

When trying an xss payload using this tag it is blocked:

![[svg_blocked.png]]

Enumerate which tags and events are allowed:

*Tags*

![[Client-Side Vulnerabilities/XSS/Reflected XSS/labs/Reflected XSS with some SVG markup allowed/images/tags.png]]

*Events*

![[events.png]]


With that information try to figure out a payload to trigger the `onbegin` event:

My mistake in this lab was to place the `onbegin` event on the svg tag. As the `animatetransform` tag is the one that really triggers the event.

# Exploitation

Payload:

```HTML
<svg><animateTransform onbegin=alert(1) /></svg>
```



