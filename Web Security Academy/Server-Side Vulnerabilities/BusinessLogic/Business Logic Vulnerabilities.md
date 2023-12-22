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


## How to prevent business logic vulnerabilities

In short, the keys to preventing business logic vulnerabilities are to:

-   Make sure developers and testers understand the domain that the application serves
-   Avoid making implicit assumptions about user behavior or the behavior of other parts of the application

You should identify what assumptions you have made about the server-side state and implement the necessary logic to verify that these assumptions are met. This includes making sure that the value of any input is sensible before proceeding.

It is also important to make sure that both developers and testers are able to fully understand these assumptions and how the application is supposed to react in different scenarios. This can help the team to spot logic flaws as early as possible. To facilitate this, the development team should adhere to the following best practices wherever possible:

-   Maintain clear design documents and data flows for all transactions and workflows, noting any assumptions that are made at each stage.
-   Write code as clearly as possible. If it's difficult to understand what is supposed to happen, it will be difficult to spot any logic flaws. Ideally, well-written code shouldn't need documentation to understand it. In unavoidably complex cases, producing clear documentation is crucial to ensure that other developers and testers know what assumptions are being made and exactly what the expected behavior is.
-   Note any references to other code that uses each component. Think about any side-effects of these dependencies if a malicious party were to manipulate them in an unusual way.

Due to the relatively unique nature of many logic flaws, it is easy to brush them off as a one-time mistake due to human error and move on. However, as we've demonstrated, these flaws are often the result of bad practices in the initial phases of building the application. Analyzing why a logic flaw existed in the first place, and how it was missed by the team, can help you to spot weaknesses in your processes. By making minor adjustments, you can increase the likelihood that similar flaws will be cut off at the source or caught earlier in the development process.


