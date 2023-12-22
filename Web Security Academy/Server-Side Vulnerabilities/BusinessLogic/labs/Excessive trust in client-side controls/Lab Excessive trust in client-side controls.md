# Lab: Excessive trust in client-side controls
#WRITEUP 
#LOGICFLAWS
<hr>

The lab will tell the vulnerability straight away, so just the exploitation phase is required.

## Exploitation

First login, then go to the leather jacket product and add it to the cart intercepting the request that is made.

![[price.png]]

Change the original price

![[price_changed.png]]

Next go to the cart and note that the price is now significantly lower, finally buy the jacket.

Lab solved.