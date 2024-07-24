
This lab is built on Node.js and the Express framework. It is vulnerable to server-side [prototype pollution](https://portswigger.net/web-security/prototype-pollution) because it unsafely merges user-controllable input into a server-side JavaScript object. This is simple to detect because any polluted properties inherited via the prototype chain are visible in an HTTP response.

To solve the lab:

1. Find a prototype pollution source that you can use to add arbitrary properties to the global `Object.prototype`.
2. Identify a gadget property that you can use to escalate your privileges.
3. Access the admin panel and delete the user `carlos`.

You can log in to your own account with the following credentials: `wiener:peter`

# Solution

The most evident functionality for testing this vulnerability is the update user form. Try capturing the request and injecting a test property:

![[update-funct.png]]

Manipulating the request I was able to detect the vuln:

![[detection.png]]

Defined properties are reflected within the response, now it's obvious that I need to set the `isAdmin` property to true, making all users administrators:

![[priv-esc.png]]

Now the admin panel is accessible:

![[Advanced Topics/Prototype pollution/Server-side prototype pollution/labs/Privilege escalation via server-side prototype pollution/images/admin-panel.png]]
