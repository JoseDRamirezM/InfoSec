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

Even if the attacker can't create their own account, using techniques such as XSS, an attacker could steal another user's "remember me" cookie and deduce how it's constructed. If the websites was built using an open-source framework, the details of the construction of the cookie may be publicly available.

In other rare cases, the user's password can be obtained if the cookie contains a hash of a well-known password, which makes decrypting the hash trivial. This demonstrates the importance of salt in effective encryption.

[[Offline password cracking]]

<hr>

# Resetting user passwords
It's common for websites to have a way to reset users passwords in case the user forgets it. Which rely on alternative methods to authenticate the user before resetting the password. For this reason password reset functionality is inherently dangerous and needs to be implemented securely.

There's a few ways that websites do this with varying degrees of vulnerability.

## Sending passwords by email
It is imperative when implementing this functionality to send a new password to the user email (never the current password). Also the sent password should expire after a very short period or the user changing their password again immediately. Otherwise this approach is highly susceptible to man-in-the-middle attacks.

Email is also generally not considered secure given that inboxes both persistent and not designed to store confidential information. Many users sync their inbox between multiple devices across insecure channels.

## Resetting passwords using an URL
A more robust method involve sending an URL that points to a password reset page. Less secure implementations use an URL with an easily guessable parameter to identify which account is being reset:

```URL
http://vulnerable-website.com/reset-password?user=victim-user
```

An attacker could change the `user` parameter to any username they know. Then the would be taken to the password change page, where they can potentially set a new password for an arbitrary user.

More secure implementations generate a high-entropy, hard to guess token and create the URL based on that. In the best case scenario, this URL should provide no hints about which user password is being reset.

## Exploitation example

[[Password reset broken logic]]

If the URL in the rest email is generated dynamically, this may also be vulnerable to password reset poisoning. In this case, an attacker could potentially steal another user's token and use it to change the user password. 

[[Password reset poisoning via middleware]]

<hr>

# Changing user passwords
Typically, changing a password involves entering the current password and then the now password twice. These pages can be also vulnerable to brute-forcing because they rely on the same process of checking that usernames and passwords match as a regular login page does.

Password change functionality is particularly dangerous if it allows an attacker to access it directly without being logged in as the victim user. As an example, if the username in provided in a `<hidden>` field an attacker could enumerate usernames and brute-force passwords changing the field value.

## Exploitation example

