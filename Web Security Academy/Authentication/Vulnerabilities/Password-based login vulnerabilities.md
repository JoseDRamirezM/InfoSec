# Password-based login vulnerabilities

This section contains the most common vulnerabilities is password-based authentication and how to exploit them. The mechanism works by providing the user with a username and a secret password via registration or by an administrator, which allow the users to authenticate.

The validity of the user identity resides in the secret password. Consequently, the security of the website would be compromised if an attacker is able to obtain or guess the login credentials of another user.

The various ways to achieve this are explored below.

## Brute-force attacks

An attacker uses a system of trial and error in an attempt to guess valid user credentials. These attacks are normally automated using wordlists of usernames and passwords. The use of dedicated tools allows an attacker to perform a vast number of login attempts at high speed.

## Brute-forcing usernames

Usernames often follow a recognizable pattern which makes them easy to guess. It is common for business logins to be `firstname.lastname@company.com` . Even if there's not a pattern high-privileged accounts use predictable usernames such as `admin` or `administrator`.

During auditing check if the website discloses potential usernames publicly. For example check for:
- Access user profile without logging in. Often the profile name is the same as the login username.
- Information leaks via HTTP responses (emails), such as administrators or IT support.

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
- **Response times**: Look for differences in the response times, if there's a considerable difference that is strong indication that the username might be correct. The website may only check if the password is correct if the username is valid, this extra computation may cause a slight delay, the attacker can make the delay more obvious by entering a excessively long password that the website takes longer to handle.



