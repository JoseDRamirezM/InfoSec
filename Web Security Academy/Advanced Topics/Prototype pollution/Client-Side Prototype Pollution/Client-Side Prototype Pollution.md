## Finding client-side prototype pollution sources manually

Finding [prototype pollution sources](https://portswigger.net/web-security/prototype-pollution#prototype-pollution-sources) manually is largely a case of trial and error. In short, you need to try different ways of adding an arbitrary property to `Object.prototype` until you find a source that works.

When testing for client-side vulnerabilities, this involves the following high-level steps:

1. Try to inject an arbitrary property via the query string, URL fragment, and any JSON input. For example:
    
    `vulnerable-website.com/?__proto__[foo]=bar`
2. In your browser console, inspect `Object.prototype` to see if you have successfully polluted it with your arbitrary property:
    
    `Object.prototype.foo // "bar" indicates that you have successfully polluted the prototype // undefined indicates that the attack was not successful`
3. If the property was not added to the prototype, try using different techniques, such as switching to dot notation rather than bracket notation, or vice versa:
    
    `vulnerable-website.com/?__proto__.foo=bar`
4. Repeat this process for each potential source.

If neither of these techniques is successful, you may still be able to [pollute the prototype via its constructor](https://portswigger.net/web-security/prototype-pollution/client-side#prototype-pollution-via-the-constructor). We'll cover how to do this in more detail later.

## Finding client-side prototype pollution sources using DOM Invader

As you can see, finding prototype pollution sources manually can be a fairly tedious process. Instead, we recommend using DOM Invader, which comes preinstalled with Burp's built-in browser. DOM Invader is able to automatically test for prototype pollution sources as you browse, which can save you a considerable amount of time and effort.

For more information, check out the [DOM Invader documentation](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/prototype-pollution#detecting-sources-for-prototype-pollution).

## Finding client-side prototype pollution gadgets manually

Once you've [identified a source](https://portswigger.net/web-security/prototype-pollution/client-side#finding-client-side-prototype-pollution-sources-manually) that lets you add arbitrary properties to the global `Object.prototype`, the next step is to find a suitable gadget that you can use to craft an exploit. In practice, we recommend [using DOM Invader](https://portswigger.net/web-security/prototype-pollution/client-side#finding-client-side-prototype-pollution-gadgets-using-dom-invader) to do this, but it's useful to look at the manual process as it may help solidify your understanding of the vulnerability.

1. Look through the source code and identify any properties that are used by the application or any libraries that it imports.
    
2. In Burp, enable response interception (**Proxy > Options > Intercept server responses**) and intercept the response containing the JavaScript that you want to test.
    
3. Add a `debugger` statement at the start of the script, then forward any remaining requests and responses.
    
4. In Burp's browser, go to the page on which the target script is loaded. The `debugger` statement pauses execution of the script.
    
5. While the script is still paused, switch to the console and enter the following command, replacing `YOUR-PROPERTY` with one of the properties that you think is a potential gadget:
    
    `Object.defineProperty(Object.prototype, 'YOUR-PROPERTY', { get() { console.trace(); return 'polluted'; } })`
    
    The property is added to the global `Object.prototype`, and the browser will log a stack trace to the console whenever it is accessed.
    
6. Press the button to continue execution of the script and monitor the console. If a stack trace appears, this confirms that the property was accessed somewhere within the application.
    
7. Expand the stack trace and use the provided link to jump to the line of code where the property is being read.
    
8. Using the browser's debugger controls, step through each phase of execution to see if the property is passed to a sink, such as `innerHTML` or `eval()`.
    
9. Repeat this process for any properties that you think are potential gadgets.

## Finding client-side prototype pollution gadgets using DOM Invader

As you can see from the previous steps, manually identifying prototype pollution gadgets in the wild can be a laborious task. Given that websites often rely on a number of third-party libraries, this may involve reading through thousands of lines of minified or obfuscated code, which makes things even trickier. DOM Invader can automatically scan for gadgets on your behalf and can even generate a DOM [XSS](https://portswigger.net/web-security/cross-site-scripting) proof-of-concept in some cases. This means you can find exploits on real-world sites in a matter of seconds rather than hours.

For more information, check out [Scanning for prototype pollution gadgets with DOM Invader](https://portswigger.net/burp/documentation/desktop/tools/dom-invader/prototype-pollution#scanning-for-prototype-pollution-gadgets).

[[DOM XSS via client-side prototype pollution]]

[[DOM XSS via an alternative prototype pollution vector]]

## Prototype pollution via the constructor

So far, we've looked exclusively at how you can get a reference to prototype objects via the special `__proto__` accessor property. As this is the classic technique for prototype pollution, a common defense is to strip any properties with the key `__proto__` from user-controlled objects before merging them. This approach is flawed as there are alternative ways to reference `Object.prototype` without relying on the `__proto__` string at all.

Unless its [prototype is set to `null`](https://portswigger.net/web-security/prototype-pollution/preventing#preventing-an-object-from-inheriting-properties), every JavaScript object has a `constructor` property, which contains a reference to the constructor function that was used to create it. For example, you can create a new object either using literal syntax or by explicitly invoking the `Object()` constructor as follows:

```
let myObjectLiteral = {}; 
let myObject = new Object();
```

You can then reference the `Object()` constructor via the built-in `constructor` property:

```
myObjectLiteral.constructor // function Object(){...} myObject.constructor // function Object(){...}
```

Remember that functions are also just objects under the hood. Each constructor function has a `prototype` property, which points to the prototype that will be assigned to any objects that are created by this constructor. As a result, you can also access any object's prototype as follows:

`myObject.constructor.prototype // Object.prototype myString.constructor.prototype // String.prototype myArray.constructor.prototype // Array.prototype`

As `myObject.constructor.prototype` is equivalent to `myObject.__proto__`, this provides an alternative vector for prototype pollution.

## Bypassing flawed key sanitization

An obvious way in which websites attempt to prevent prototype pollution is by sanitizing property keys before merging them into an existing object. However, a common mistake is failing to recursively sanitize the input string. For example, consider the following URL:

`vulnerable-website.com/?__pro__proto__to__.gadget=payload`

If the sanitization process just strips the string `__proto__` without repeating this process more than once, this would result in the following URL, which is a potentially valid prototype pollution source:

`vulnerable-website.com/?__proto__.gadget=payload`

[[Client-side prototype pollution via flawed sanitization]]

## Prototype pollution in external libraries

As we've touched on already, prototype pollution gadgets may occur in third-party libraries that are imported by the application. In this case, we strongly recommend using DOM Invader's prototype pollution features to identify sources and gadgets. Not only is this much quicker, it also ensures you won't miss vulnerabilities that would otherwise be extremely tricky to notice.

