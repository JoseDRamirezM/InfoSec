# Methodology

#COMMANDINJECTION 
#METHODOLOGY 
<hr>

Test request parameters appending commands with command separator characters and look for the application output for any hint that a OS command was executed. Have in mind that all commands are system dependent.

Test the vulnerability as follows:

1. Inject simple commands in parameters with command separators. It may be necessary to URL encode the payload.

`parameter1=value&parameter2=URLEncode(&whoami)`

## Useful commands

Purpose of command | Linux | Windows
---------------|-------|------------
Name of current user |`whoami`|`whoami`
Operating system | `uname -a` | `ver`
Network configuration | `ifconfig` | `ipconfig /all`
Network connections | `netstat -an` | `netstat -an`
Running processes | `ps -ef` |`tasklist`

