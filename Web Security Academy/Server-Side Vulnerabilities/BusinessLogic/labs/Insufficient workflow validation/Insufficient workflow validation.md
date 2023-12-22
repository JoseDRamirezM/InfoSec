# Insufficient workflow validation

#LOGICFLAWS 
#WRITEUP 
<hr>

## Recon

Interact with the application and try to exploit the purchasing workflow to buy a "Lightweight l33t leather jacket".

- Determine the workflow and it's requests
	1. Add product to cart
	2. Go to cart
	3. Place order

![[funds.png]]

Simply add the Jacket to the cart, next place the order and change the response `Location` to:

```HTTP
Location: /cart/order-confirmation?order-confirmed=true
```

And the lab is solved.