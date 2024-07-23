This lab is vulnerable to DOM XSS via client-side prototype pollution. To solve the lab:

1. Find a source that you can use to add arbitrary properties to the global `Object.prototype`.
    
2. Identify a gadget property that allows you to execute arbitrary JavaScript.
    
3. Combine these to call `alert()`.
    

You can solve this lab manually in your browser, or use [DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader) to help you.


# Recon

For this lab, DOM Invader really does all the heavy lifting for finding the prototype pollution and finding a gadget to get DOM XSS:

![[Advanced Topics/Prototype pollution/Client-Side Prototype Pollution/labs/DOM XSS via client-side prototype pollution/images/dom-invader.png]]

Scan for gadgets on each case, in the end the first case is the only exploitable finding:

![[scan-complete.png]]

![[Advanced Topics/Prototype pollution/Client-Side Prototype Pollution/labs/DOM XSS via client-side prototype pollution/images/solved.png]]


# Manual testing

1. Inject in the query string:

```
/?__proto__[foo]=bar
```

2. In the console type:

```
Object.prototype
```

![[detected-pollution.png]]

3. Identify a gadget
	1. Study the client-side code executed by the application searching for a sink

![[Advanced Topics/Prototype pollution/Client-Side Prototype Pollution/labs/DOM XSS via client-side prototype pollution/images/sink.png]]

4. Craft an exploit

Knowing that the code uses the `transport_url` property within a script element manipulate the prototype attribute to place `alert(1)` as the value of this property:

```
/?__proto__[transport_url]=data:,alert(1);
```

After doing this the DOM will be injected with:

![[DOM-injected.png]]

Successfully executing the passed Javascript code

