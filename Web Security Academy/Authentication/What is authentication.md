# What is authentication
#AUTHENTICATION 
#FACTORS

The process of verifying the identity of a given user or client. In simple words making sure that they are really who they claim to be. As websites are exposed to the internet, robust authentication mechanisms are key for effective web security.

## Authentication factors

There are three factors in which authentication can be categorized:

- Something you `know` such as a **password** or the answer to a **security question**. AKA `knowledge factors`.
- Something you `have` such as a physical object or a security token. AKA `posession factors`.
- Something you `are` or do such as biometrics or patterns of behavior. AKA `inherece factors`.

Authentication mechanisms rely on a range of technologies to verify one or more of these factors.

## Authentication and authorization

### Authentication

Verify that a user is who they claim to be.

### Authorization

Verify that a user is allowed to do something.

In the context of a web page `authentication` determines if the attempted access of a given username `testest` is really who created the account. Once the user is authenticated, the permissions of that user determines if he is authorized to perform actions on the website.

## How authentication vulnerabilities arise

Broadly speaking there are two ways:

- The authentication mechanisms are weak and vulnerable to brute force attacks.
- Logic flaws or poor implementation allows authentication controls to be bypassed. This is also called `Broken Authentication`.

In many cases `logic flaws` cause the website to behave unexpectedly, though as authentication is critical to security these flaws have a great potential to expose the website to security issues.

## The impacts of vulnerable authentication

Once authentication controls are bypassed:
- Access data and functionality that the compromised account has, depending on the privileges (regular user, administrator) the impacts are more severe and potentially give access to the internal infrastructure.
- Expand the attack surface.

Often high-severity attacks are not possible from a publicly accessible page, but from an internal page.

[[Vulnerabilities in authentication mechanisms]]