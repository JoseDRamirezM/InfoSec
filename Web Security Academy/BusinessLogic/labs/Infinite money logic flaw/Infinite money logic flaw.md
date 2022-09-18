# Infinite money logic flaw

#LOGICFLAWS 
#WRITEUP 
<hr>

## Recon

The e-commerce application has a logic flaw in the purchasing flow.

## Assessment

The vulnerability consists of two functionalities that can be abused that are:

- The news teller coupon
- Gift card 

When buying a gift card and applying the discount of the coupon, an attacker can then redeem the bought gift cards in the same account and "gain" the discount credit. Which ultimately allows to accumulate credit indefinitely.

## Exploitation

The exploitation method that I followed to somehow  automate some steps are:

1. Add to cart the maximum possible gift cards
2. Apply the discount coupon
3. Send the request to redeem the gift cards to the Intruder
4. Paste the obtained gift card codes as payloads and execute the attack

Repeat the steps above until the user accumulates enough credit to buy the jacket to solve the lab.

![[payload_posi.png]]

![[abuse_gift_card.png]]


From there accumulate credit.

I recommend sending each request of the process in to the Repeater, to make the process even faster.

