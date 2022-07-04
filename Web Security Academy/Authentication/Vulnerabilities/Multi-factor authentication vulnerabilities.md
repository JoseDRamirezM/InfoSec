# Multi-factor authentication vulnerabilities
#AUTHENTICATION 
#THEORY

<hr>

Multiple authentication factors allow an user to prove their identity apart from credentials. The most common way to do that is `two-factor authentication` (2FA) (As verifying biometric factors is impractical) based on something the user `knows` and something the user `have`. The process requires users to enter a traditional password and a temporary verification code from an out-of-band physical device in their possession.

These mechanisms increase security by reducing the chance of an attacker to obtain the secret password and the other factor from the out-of-band source. However this measures are as secure as its implementation. Poorly implemented 2FA can be beaten or even bypassed entirely.

Full benefits from 2FA come from verifying multiple `different` factors. Verifying the same factor twice it's not `true 2FA`, an example of this is email-based 2FA, even though the user has to provide a password and a verification code, accessing the code relies on knowing the login credentials for their email account.

<hr>

# Two-factor authentication tokens

Verification codes are often read by the user form a physical device. High-security websites provide a dedicated device, such as the RSA token or keypad device that is used to access online banking or work laptop. 

![[RSA_token.png]]![[RSA_keypad.png]]

These devices generate the verification code directly. Other common practice is to use a dedicated mobile app, such as Google Authenticator.

On the other hand, websites often send verification codes to a user's mobile phone as a text message. While this is `something the user has` it can be abused. Firstly, the code is transmitted via SMS, which can be potentially intercepted. Also there's a risk for SIM swapping, whereby an attacker fraudulently obtains a SIM card with the victim's phone number. The attacker would then receive all SMS messages sent to the victim, successfully intercepting the verification code.

# Bypassing two-factor authentication

Flawed implementation of 2FA might allow an attacker to bypass it entirely. If the user enters a password, and then a verification code in a other page, the user is in a "logged in" state before the verification code is entered. In those cases it's important to try to access "logged in only" pages after completing the first authentication step. Occasionally it may be found that the website doesn't actually check whether the user completed the second step before loading the page.

## Exploitation example

[[2FA simple bypass]]

<hr>

# Flawed two-factor verification logic

Often times the 2FA logic doesn't adequately verify the same user is completing the second step. Picture the following scenario:

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

## Exploitation example

[[2FA broken logic]]

<hr>

# Brute-forcing 2FA verification codes

Websites need to take measures to prevent brute-forcing of the 2FA verification codes. As this codes are often 4 or 6 digit numbers cracking them is trivial.

Some websites attempt to prevent this by automatically logging a user out if a certain number of incorrect attempts are made. This is not effective as an advanced attacker can automate this multi-step process by creating macros for Burp Intruder or using Turbo Intruder.
