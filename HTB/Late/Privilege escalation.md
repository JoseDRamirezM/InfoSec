# Privilege escalation

After getting access to the server via RCE:

## User and machine enumeration

I used linpeas to enumerate the machine.

I found that the `/usr/local/sbin` path is writable and also the user `svc_acc` owns the following script:

Writable path:

![[writable.png]]

Script:


![[script.png]]

![[script_access.png]]

Check what the script does

![[ssh-alert.png]]

It sends an alert to the root user email each time an user logs in via SSH to the machine. The weird thing was that there was no visible cron job of any user calling that task.

I was introduced to [pspy](https://github.com/DominicBreuker/pspy)  a python tool to `snoop` on the system processes without root permissions. The only way  to see if the script is really triggered when an user logs in via SSH is to run `pspy` and log in to another SSH session. Doing that revealed the following:

![[root_exec_script.png]]

Even though wasn't possible to edit the script in order to place a reverse shell. The `svc_acc` user can only append to the script file. Verify that with the `lsattr` command and look for the `a` flag.

![[lsattr.png]]

Create a file with a reverse shell payload and append it to the script via stdin.

![[evil.png]]

![[append.png]]

Then start a listener and start a new SSH session to trigger the script.

## Root shell

A root shell is obtained, capture the root flag and the machine is solved.

![[path_abuse.png]]

The privilege escalation is possible due to a path abuse, as the `svc_acc` user has control over a script that root executes, even though the script is present in the root folder the PATH forces the execution of the `svc_acc` user script.

![[root_script.png]]

[[Vulnerability report]]