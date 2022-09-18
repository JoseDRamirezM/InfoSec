# Making flawed assumptions about user behavior

#LOGICFLAWS 
#THEORY 
<hr>

Is one of the main reasons logic vulnerabilities arise. The user is able to interact in scenarios that violates these assumptions and possibly the developers didn't contemplate them.

## Trusted users won't always remain trustworthy

Applications that strongly enforce business rules seem secure, but it assumes that when these strict controls have been passed, the related user and his data can be trusted indefinitely.

This can create loopholes that can be exploited.

### Exploitation example
[[Inconsistent security controls]]
<hr>

## Users won't always supply mandatory input

Client-side controls for mandatory fields work on regular users. But attackers can bypass these controls easily. Tampering or even removing parameters.

This becomes an issue when multiple functions are implemented in the same the server-side script, where the presence of certain parameter determines which code is executed. By removing parameters an attacker may access code paths that are supposed to be out of reach.

When testing for logic flaws try removing each parameter in turn and observing what effect this has on the response, having in mind:

- Remove one parameter at a time
- Delete both the value and the name of the parameter in different tests (usually the server handle both cases differently)
- Follow multi-step processes, removing parameters in one step may affect another in the workflow

Test
- GET parameters
- POST parameters
- Cookies

### Exploitation example

[[Weak isolation on dual-use endpoint]]
[[Password reset broken logic]]

## Users won't always follow the intended sequence

Many transactions rely in predefined workflows consisting of a series of steps. The web interface will guide the user for each step. Attackers may not adhere to the sequence and if the application doesn't consider this it can lead to dangerous flaws.

For example, many websites that implement two-factor authentication (2FA) require users to log in on one page before entering a verification code on a separate page. Assuming that users will always follow this process through to completion and, as a result, not verifying that they do, may allow attackers to bypass the 2FA step entirely.

### Exploitation example

[[2FA simple bypass]]

Using a proxy allows an attacker to interact with the workflows in any order. This allows to perform actions while the application is in an unexpected state.

#IMPORTANT
To identify these vulnerabilities, use forced browsing to submit requests in an unintended sequence i.e

- Skip some steps
- Access one step more than once
- Return to earlier steps
- Submitting different sets of parameters in each request

Try to identify which assumptions developers have made and where the attack surface lies. This kind of testing may cause exceptions because expected variables have null or uninitialized state.

Pay close attention to error/debug messages as they can be the source of information disclosure, which can help to fine-tune attacks and understand details about the back-end behavior.

## More exploitation examples

- [[Insufficient workflow validation]]
- [[Authentication bypass via flawed state machine]]