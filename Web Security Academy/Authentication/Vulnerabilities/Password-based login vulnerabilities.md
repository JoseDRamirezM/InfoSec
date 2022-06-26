# Password-based login vulnerabilities
<hr>

This section contains the most common vulnerabilities is password-based authentication and how to exploit them. The mechanism works by providing the user with a username and a secret password via registration or by an administrator, which allow the users to authenticate.

The validity of the user identity resides in the secret password. Consequently, the security of the website would be compromised if an attacker is able to obtain or guess the login credentials of another user.

The various ways to achieve this are explored below.
<hr>
## Brute-force attacks

An attacker uses a system of trial and error in an attempt to guess valid user credentials. These attacks are normally automated using wordlists of usernames and passwords. The use of dedicated tools allows an attacker to perform a vast number of login attempts at high speed.
<hr>
## Brute-forcing usernames

Usernames often follow a recognizable pattern which makes them easy to guess. It is common for business logins to be `firstname.lastname@company.com` . Even if there's not a pattern high-privileged accounts use predictable usernames such as `admin` or `administrator`.

During auditing check if the website discloses potential usernames publicly. For example check for:
- Access user profile without logging in. Often the profile name is the same as the login username.
- Information leaks via HTTP responses (emails), such as administrators or IT support.
<hr>
## Brute-forcing passwords

The same principle applies for passwords, but the difficulty augments with the password complexity. It's common to be a password policy, which forces users to create high-entropy passwords that are harder to crack using brute-force alone. Passwords are inforced by:

-   A minimum number of characters
-   A mixture of lower and uppercase letters
-   At least one special character

Human behavior may introduce vulnerabilities by defining easy to remember passwords that fit into the password policy. Also if the policy requires the users to change their password on a regular basis, the users may make minor, predictable changes to their preferred password.

### Examples

`mypassword` --> `Myp4$$w0rd` or `Mypassword1!`

`Mypassword1!` becomes `Mypassword1?` or `Mypassword2!

Brute-force attacks can often be much more sophisticated and effective, than simply iterating over every possible combination of characters.
<hr>
## Username enumeration

Occurs when an attacker is able to observe changes in the website's behavior in order to determine whether a given username is valid.

These scenarios often arises on the login page when a user enters:
- A valid username but an incorrect password.
- The registration form tells that a given username is already taken.

This greatly reduces the time and effort required to brute-force a login because the attacker is able to generate a list of valid usernames.

When attempting to brute-force a login page, pay attention to:
- **Status codes**: Look for differences in the response HTTP status code, if a different status code is returned from a number of guesses that is a strong indication that the username was correct. It is best practice that the website returns the same status code regardless of the outcome.
- **Error messages**: The error message may change if:
	- Username and password are incorrect.
	- Only the password is incorrect.
t is best practice that the website returns the same generic message regardless of the outcome. Also look out for minor differences and even non-visible characters on the page.
- **Response times**: Look for differences in the response times, if there's a considerable difference that is strong indication that the username might be correct. The website may only check if the password is correct if the username is valid, this extra computation may cause a slight delay, the attacker can make the delay more obvious by entering a excessively long password that the website takes longer to handle. For this attack to work it's important to provide a very long password to make the delays evident.

## Exploitation examples
- [[Username enumeration via different responses]]
- [[Username enumeration via subtly different responses]]
- [[Username enum
eration via response timing]]

<hr>
# Flawed brute-force protection
Brute force attacks are noisy, requiring many requests before an attacker can compromise an account. Logically brute-force protection revolves around making it really hard to automate the process and to slow down the rate at which login attempts are made. The most common ways of preventing brute-force attacks are:

- Locking the account that a remote user is trying to access, if many failed login attempts are made.
-  Blocking the remote user's IP address if too many login attempts are made in series.

Both methods offer varying degrees of protection, but neither is invulnerable, especially if implemented using flawed logic.

## Example

It's common to encounter an IP block if the user fails to log in too many times. In some cases the counter for the failed attempts resets if the IP owner logs in successfully. This means that the attacker would simply login to their own accounts every few attempts to prevent reaching the limit.

Including attacker controlled credentials at regular intervals throughout the wordlist is enough to make this defense useless.

## Exploitation examples

- [[Broken brute-force protection IP block]]

<hr>

# Account locking

Websites try to prevent brute-forcing by locking the account if a certain suspicious criteria are met, usually a set number of failed login attempts. If the server indicates that an account is blocked, it can help an attacker to enumerate users.

This approach offers protection against targeted brute-forcing of an specific account. But it fails when the attacker want to gain access to any random account.

The scenario in which the attacker has both a set of valid usernames and a short list of potential passwords, the attacker can try the credentials on each account (the number of passwords depends on the limit of failed attempts) without locking the accounts.

## Exploitation example

[[Username enumeration via account lock]]

<hr>

# User rate limiting

If an IP address makes too many login requests wihtin a short period of time the IP address is blocked. IT can be unblocked by:

- Automatically after a certain period of time.
- Manually by an administrator.
- Manually by the user after successfully completing a CAPTCHA.

This approach is often preferred as it is less prone to user enumeration and denial of service attacks. However this is still not completely secure. There are many ways to manipulate the apparent IP in order to bypass the block.

As the limit is based on the rate of HTTP requests sent from the user's IP address, this can be bypassed if there's a way to guess multiple passwords with a single request.

## Exploitation example

[[Broken brute-force protection, multiple credentials per request]]

<hr>

# HTTP Basic authentication

It's a simple and old mechanism. The client receives an authentication token from the server, which is constructed by concatenating the username and password and encoding it in `Base64`. Then the token is placed on the `Authorization` header of every subsequent request.

```HTTP
Authorization: Basic base64(username:password)
```

This is not considered a secure authentication method. If HSTS (HTTP Strict Transport Security read more [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)) is not implemented, the user credentials are open to be captured on a MiTM (Man in The Middle) attack.

HTTP Basic authentication does not support protection against brute-force attacks and it's vulnerable to session-related exploits, notably CSRF, which it can't mitigate on its own.

In some cases, exploiting HTTP basic authentication might only grant an attacker access to an irrelevant page. But it expands the attack surface and also the credentials might be reused on other sensitive context.