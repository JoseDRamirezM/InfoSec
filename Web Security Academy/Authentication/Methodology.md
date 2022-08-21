# Methodology
<hr>
The scope of these tests is mostly the login page of a website.
<hr>
## Password based login

### Brute-force attacks

Check if it is possible to brute-force user passwords and if there's no protection against it, using these techniques.

- Check if some kind of `IP block protection` is present and try to bypass it by:
	- Creating a custom wordlist where at a constant number of tries valid credentials are provided hoping to reset the counter and being able to test all the candidate passwords.
	[[Broken brute-force protection IP block]]
- Check if it's possible to send more than one password in a request (mostly when JSON APIs are used). Try to send an array of passwords.
	![[multiple.png]]
[[Broken brute-force protection, multiple credentials per request]]


### User enumeration

Test this by providing a wordlist with multiple users with a test password, identify this vulnerability by checking:

#### Status codes

A different status code arising after a number of tries may be an indication of a valid user.

#### Response differences

Check for differences in the responses that may indicate that the user is valid.

[[Username enumeration via different responses]]

These differences can be very subtle pay close attention!

[[Username enumeration via subtly different responses]]

#### Response timing

Provide an excessively long password and look for differences in the response time, this can indicate that an user is valid, because the extra computation of the password could create a slight delay in the response.

[[Username enumeration via response timing]]

#### Account locking

When account locking is implemented check for differences in the response length that may indicate that the user is valid (a message warning that the account was blocked), when trying to guess the password of an user with a constant amount of attempts.

[[Username enumeration via account lock]]

<hr>
## Multi-factor based login

### 2FA simple bypass

Check if the user is in a `logged in` state without providing a valid verification code by trying to access `logged in only` pages after completing the first authentication step.

Exploitation example [[2FA simple bypass]]

### Flawed two factor login

Check if the application checks properly that the same user is completing the second step of the authentication flow. This scenario is clearer with the following example:

A user logs in with normal credentials in the first step.

```HTTP
POST /login-steps/first HTTP/1.1 
Host: vulnerable-website.com
... 
username=carlos&password=qwerty
```

Next the server assigns a cookie that relates to the user account, before being taken to the second step of the login process:

```HTTP
HTTP/1.1 200 OK 
Set-Cookie: account=carlos
```

```HTTP
GET /login-steps/second HTTP/1.1 
Cookie: account=carlos
```

When submitting the verification code, the requests uses the assigned cookie to determine which account the user is trying to access:

```HTTP
POST /login-steps/second HTTP/1.1 
Host: vulnerable-website.com 
Cookie: account=carlos 
... 
verification-code=123456
```

In this case, an attacker could log in using their own credentials but then change the value of the account cookie to any arbitrary username when submitting the verification code.

```HTTP
POST /login-steps/second HTTP/1.1 
Host: vulnerable-website.com 
Cookie: account=victim-user 
... 
verification-code=123456
```

This is extremely dangerous if the attacker is able to brute-force the verification code as it would allow to log in to arbitrary user accounts based entirely on their username, not even knowing the user's password.

Exploitation example [[2FA broken logic]]

### Brute-forcing 2FA verification codes

As verification codes are often 4 to 6 characters long, cracking them is trivial, test this in the following scenarios:

1. 2FA without brute force protection

In this scenario use burp Intruder to figure out the correct code, making sure the request contains whatever mechanism to authenticate as the target user.

2. 2FA with brute force protection

When some kind if protection is implemented (session handling with a CSRF token or logging out a user after a number of tries) try to use `Macros` to handle a custom `flow` or `sequence` of requests that have to be made in order to perform the attack more on that in this lab [[2FA bypass using a brute-force attack]].



<hr>
## Other authentication mechanisms

### Brute force a stay logged in cookie

Check for functionalities like:
- Remember me
- Keep me logged in

Then check the site generated cookies and test if it is possible to reverse the contents in which the cookie was created (often user related information), or even using brute force, in an attempt to bypass the login process for other user account.

If it is possible try using Burp Intruder and processing the payload in order to generate a valid cookie.

Exploitation example [[Brute-forcing a stay-logged-in cookie]]

### Offline password cracking

If an XSS vulnerability is found try to steal a `Stay logged in` cookie from other user, depending on how it is constructed it may be possible to obtain sensitive information about the user (username, password).

Exploitation example [[Offline password cracking]]

<hr>
## Password reset functionalities

#### Broken logic

Test the necessary steps for a password reset, checking if it is possible to change other user password altering the information sent in each request pointing to other username.

Exploitation example [[Password reset broken logic]]

#### Password reset poisoning

Trick the application server to send the password reset request containing a secret token for a specific user to an attacker controlled site.

Exploitation example [[Password reset poisoning via middleware]]



## Password change

Test thoroughly the password change form, looking for information that the site may provide which strongly indicates that an user current password is correct i.e. the form gives an error message like `New passwords do not match` when the user password is correct but the new password and its confirmation don't match.

Exploitation example [[Password brute-force via password change]]