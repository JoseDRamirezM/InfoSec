#  OAST : Out-of-band Application Security Testing

## Context

It uses external servers to see otherwise invisible vulnerabilities. It was introduces to further improve the DAST (Dynamic Application Security Testing) model.

It offers two major benefits:

- Detect invisible vulnerabilities: When executing DAST blind and asynchronous bugs are easily missed.
- False positives: The SAST approach of security testing tend to produce many false positives, which costs time and money.

## How it works

OAST improves the results of DAST, maintaining the `outside` approach.

### Attacking from the outside

DAST essence is to send payloads to a target application and analyze the responses that come back, just like a real attacker might.

When a vulnerability is discovered it's `assured` by the application's response to some payload, that suggests a vulnerability. The problem that OAST solves is that if the target app does not return a response to a payload, even though the target is actually vulnerable. This happens when the app works asynchronously. Traditional DAST techniques won't see it.

### See over the horizon

OAST is based on the `Burp Collaborator` tool, that allows to detect a new range of vulnerabilities, including **blind SQL injection**, **blind Cross Site Scripting** and **blind Command Injection** vulnerabilities.

It provides a new channel of communication into the DAST process.

![[collaborator.png]]

When working with **blind** vulnerabilities, no useful information is sent into the response (even if the attack is successful). The need to bypass this scenario is where OAST comes into play. Once an attack payload is sent causing an interaction with an external system we have control over, that is outside the target domain.

The `Burp Collaborator` is a configured server to detect `Burp Scanner` payloads to catch any triggered action by those payloads.


![[OAST advantages.png]]

