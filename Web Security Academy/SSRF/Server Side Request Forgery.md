#SSRF
#THEORY 

<hr>


## What is SSRF?

It's a web security vulnerability that allows an attacker  to perform arbitrary requests server-side to an unintended location.

This may cause the server to make connections to internal-only services within the organization's infrastructure, or force a connection to external systems, potentially leaking sensitive data such as authorization credentials.

## What is the impact of SSRF attacks?

Possible impacts are:
- Unauthorized actions or access to data
- Arbitrary command execution
- Allow further attacks that appear to originate from the application hosting service

## Common SSRF attacks

Often, trust relationships between the server and other back-end systems are exploited to escalate an attack from the vulnerable application to perform unauthorized actions.

[[SSRF exploitation techniques]]




