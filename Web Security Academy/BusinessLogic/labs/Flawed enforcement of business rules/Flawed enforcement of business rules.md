# Flawed enforcement of business rules

#LOGICFLAWS 
#WRITEUP 
<hr>

## Recon

The same e-commerce application from previous labs, but this time there's an announcement about a discount code.

![[discount_code.png]]

That gives a hint about where to look.

There's also another discount code that is obtained after completing the news teller susbscription at the bottom of the page.

![[discount_code_1.png]]

## Assessment

The first coupon gives a $5 discount, the second coupon gives a discount to a percentage of the total price.

## Exploitation

The coupons can be entered in series as follows:

![[BusinessLogic/labs/Flawed enforcement of business rules/images/exploit.png]]

Which will allow to buy the jacket and the lab is complete.