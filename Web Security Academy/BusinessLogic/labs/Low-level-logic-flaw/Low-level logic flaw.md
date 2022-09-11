# Low-level logic flaw

#LOGICFLAWS 
#WRITEUP 
<hr>

## Recon

The app won't allow negative values on the quantity parameter, when adding them to the cart. Instead it will remove the item from the cart.

## Exploitation

By sending an enormous amount of requests telling the server to add to the cart any item with  `quantity=99`, as only two numbers are allowed on this parameter. 

![[req.png]]

The idea is to do this until the variable that hold the `Total Price` value in the `/cart` reaches it's maximum value. To effectively exploit this scenario Burp Intruder (I didn't use this), ZAP or TurboIntruder can be used.

In ZAP, use the fuzzer sending null payloads until it's easy to add X quantity of another product so the total price is less than a $100 that are the funds the provided user has.

![[progress.png]]

For Turbo intruder I used the following script:

![[turboIntruder.png]]

Also note it's important to set a high value for the concurrentConnections parameter to make it faster.

Either approach will lead to the same result

![[suitable.png]]

When a reasonable negative total has been reached add the necessary quantity of other product so that it's affordable.

![[final.png]]

Lastly place the order and the lab is solved!