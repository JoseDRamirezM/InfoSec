# Blind SQL injection
#BLINDSQLI

## Context

Many of the SQL injection vulnerabilities are blind. This means the application does not return of the SQL query or the details of any database errors within its responses. Blind vulnerabilities can be exploited to access data but the techniques involved are more complicated and difficult to perform.

	Blind --> No database content or errors in the response

## Techniques

Depending on the scenario the following techniques can be applied to exploit blind SQL injection vulnerabilities:

- Change/inject the logic of the query or place a condition that generates a detectable difference in the application's response. This might involve injecting a new condition into some Boolean logic or conditionally triggering an error such ad divide-by-zero.
- Conditionally trigger a time delay to infer the truth of the condition based on the time that the application takes to respond.
- The use of [[OAST]] techniques. Which can detect vulnerabilities that normally are missed. For example it's possible to exfiltrate data via the out-of-band channel, placing data into a DNS lookup for a domain that the attacker controls.

## What is blind SQL injection?

The vulnerability arises when an application is vulnerable to SQL injection, but the HTTP responses don't contain the results of the relevant SQL query or the details of any database errors.

The techniques used to exploit this vulnerability differ from traditional SQL injection techniques, as there's no way to see the results of the injected query on the application's response.

[[Exploiting blind SQL injection by triggering conditional responses]]