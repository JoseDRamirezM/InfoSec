# Password reset poisoning
#THEORY 
#AUTHENTICATION 

<hr>

It's a technique in which an attacker manipulates a vulnerable website into generating a password reset link pointing to a domain under the attacker's control. This can be leveraged to obtain secret tokens required to reset arbitrary user's passwords and ultimately compromise their accounts.

## How does a password reset work?

If the URL that is sent to the user is dynamically constructed based on controllable input, such as the host header, it may be possible to construct a password reset poisoning attack.

1. The attacker obtains the victim's email address or username and submits a password reset request on their behalf. When submitting the form the corresponding HTTP request is intercepted, the `Host` header is then modified so it points to an attacker controlled domain.
2. The victim receives a genuine password reset email directly from the website. Containing the reset password link and token in which the domain name points to the attack server.

```
https:evil.com/reset?token=sadfag2321
``` 

3. If the victim clicks the link or even if it's fetched by an antivirus, the password reset token will be sent to the attacker's server.
4. The attacker will visit the real URL for the password reset, providing the obtained token and then compromising the victim's account.

In practice the attacker may seek to increase the probability of the victim clicking the link by appending some warning message or a fake breach notification. The host header often can be used to inject HTML into sensitive emails.

## Exploitation example


[[Password reset poisoning via middleware]]