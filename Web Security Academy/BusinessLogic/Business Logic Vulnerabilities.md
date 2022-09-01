# Business Logic Vulnerabilities

## What are business logic vulnerabilities?

Business logic vulnerabilities are flaws in the design and implementation of an application that allow an attacker to elicit unintended behavior. Often these are due to failing to anticipate unusual application behavior which ultimately is handled insecurely.

`Businness logic` refers to how the application operates, but can be also called `application logic vulnerabilities` or `logic flaws`.

Logic flaws are often invisible and hard to see. The exploitation requires interacting with the application in ways developers never intended. 

In simple words the rules and constraints of the application must be enforced in any given scenario and the behavior of the application must be coherent with this principle. Attackers may be able to circumvent these rules for example:

- Complete a transaction without going through the intended purchase workflow.
- Arbitrary changes in critical values of each transaction or input non nonsensical data.

These scenarios may make the application behave in unexpected ways.

Logic-based vulnerabilities depend on the application itself and its functionality. To find this type of vulnerabilities human knowledge may be necessary, making them hard to find with automated tools. As a result logic flaws are a great target for bug bounty hunters and manual testers.

## How do business logic vulnerabilities arise?

Generally from design to development flawed assumptions are made about how users will interact with the application, which leads to:

- Inadequate validation of user input e.g the developers assume that users will interact with the application exclusively via a web browser, implementing weak client-side controls. Which can be bypassed using a proxy.
- Large code bases of overly complicates systems which developers don't fully understand (as a whole), assumptions made in one component may affect another.

## Logic vulnerabilities impacts

The impact of this kind of vulnerability is highly variable, flawed logic should be fixed even if the tester can't figure out a way to exploit this, there's always a risk of someone else will be able to.

**The impact of any logic vulnerability depends on what functionality it is related to**

e.g vulnerabilities in
- Authentication mechanism may lead to privilege escalation, authentication bypass, access to sensitive data and functionality.
- Financial transactions may lead to fund loss, fraud, ...

## Examples of business logic vulnerabilities

Based on real-world cases.

[[Examples of business logic vulnerabilities]]





