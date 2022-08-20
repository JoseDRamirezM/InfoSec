# Methodology

The scope of these tests is mostly the login page of a website.

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

## Multi-factor based login

### 2FA simple bypass

Check if the user is in a `logged in` state without providing a valid verification code by trying to access `logged in only` pages after completing the first authentication step.

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

### Brute-forcing 2FA verification codes

