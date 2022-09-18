# Domain-specific flaws
#THEORY 
#LOGICFLAWS 
<hr>

Often times logic flaws are specific to the business domain or the purpose of the page. Picture this example:

```
The discounting functionality of online shops is a classic attack surface when hunting for logic flaws. This can be a potential gold mine for an attacker, with all kinds of basic logic flaws occurring in the way discounts are applied.

For example, consider an online shop that offers a 10% discount on orders over $1000. This could be vulnerable to abuse if the business logic fails to check whether the order was changed after the discount is applied. In this case, an attacker could simply add items to their cart until they hit the $1000 threshold, then remove the items they don't want before placing the order. They would then receive the discount on their order even though it no longer satisfies the intended criteria.
```

Look for:
- Situations where prices or other sensitive values are adjusted based on user actions.
- Try to understand 
	- the algorithms that the application use
	- at what point adjustments are made

**IMPORTANT TESTING NOTE**

#IMPORTANT 

Manipulate the application so that it is in a state where the applied adjustments do not correspond to the original criteria intended by the developers.

Also,
```
To identify these vulnerabilities, you need to think carefully about what objectives an attacker might have and try to find different ways of achieving this using the provided functionality. This may require a certain level of domain-specific knowledge in order to understand what might be advantageous in a given context.
```

Failing to have domain-specific knowledge may lead to miss bugs in the application.

## Exploitation examples

- [[Flawed enforcement of business rules]]
- [[Infinite money logic flaw]]