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

Test this by providing a wordlist with multiple users with a test password

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

