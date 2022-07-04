# Other authentication mechanisms vulnerabilities
#AUTHENTICATION 
#THEORY 

Explore vulnerabilities of supplementary functionality that is related to authentication. These functionalities allow users to manage their account. Things like:

- Password change.
- Password reset.

Websites must make these functionalities as secure as their login pages. This is specially important when an attacker can create their own account and interact with these pages.

<hr>

# Keeping users logged in

A common feature is to stay logged in after closing a browser session. This is often presented as "Remember me" or "Keep me logged in". This is implemented by generating a token of some kind which is stored in a persistent cookie. This cookie should be impractical to guess as it allows to bypass the entire login process. Some websites use user related information to generate the cookie, an attacker could study their own cookie and deduce how it's generated. After that brute-force techniques can be used to gain access to other users accounts.

Not properly implemented encryption or simple encoding offer no protection when applied to these cookies. Not even a one-way hash function is bulletproof, an attacker could figure out the hashing algorithm and if no salt is used, brute-forcing the cookie may be possible by hashing a wordlist. A limit on the cookie guesses must be applied also.

## Exploitation example

[[Brute-forcing a stay-logged-in cookie]]

<hr>



