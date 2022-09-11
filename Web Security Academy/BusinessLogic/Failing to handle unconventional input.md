# Failing to handle unconventional input

One aim of application logic is to restrict user input to values that adhere to the business rules. The application accept arbitrary values but the logic determines if those values are acceptable. Many constraints can be applied to manage, inventory, budget restrictions and so on.

It's important for the developers to anticipate all possible scenarios when implementing a functionality. If there is no explicit logic for handling a given case, this can lead to unexpected and potentially exploitable behavior.

Consider a funds transfer between two bank accounts. This functionality will almost certainly check whether the sender has sufficient funds before completing the transfer:

```
$transferAmount = $_POST['amount']; 
$currentBalance = $user->getBalance(); 
if ($transferAmount <= $currentBalance) 
	{ // Complete the transfer } 
else { // Block the transfer: insufficient funds }
```

But if the logic doesn't sufficiently prevent users from supplying a negative value in the `amount` parameter, this could be exploited by an attacker to both bypass the balance check and transfer funds in the "wrong" direction. If the attacker sent -$1000 to the victim's account, this might result in them receiving $1000 from the victim instead. The logic would always evaluate that -1000 is less than the current balance and approve the transfer.

Simple logic flaws like this can be devastating if they occur in the right functionality. They are also easy to miss during both development and testing, especially given that such inputs may be blocked by client-side controls on the web interface.

Test the applications using a proxy and provided corner-case data in order to answer this questions:

-   Are there any limits that are imposed on the data?
-   What happens when you reach those limits?
-   Is any transformation or normalization being performed on your input?

This may expose weak input validation that allows to manipulate the application in unusual ways.

## Exploitation examples

- [[High-level logic vulnerability]]
- [[Low-level logic flaw]]
- [[Inconsistent handling of exceptional input]]