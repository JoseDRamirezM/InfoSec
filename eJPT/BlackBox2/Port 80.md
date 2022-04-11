# Port 80

![[dirb.png]]


# Possible attack vectors

### Services vulnerabilities

I searched for Apache 2.4.29 vulnerabilities, but nothing came out. Then I looked at all Apache exploits and found one that exploits a cgi-bin script (Shellshock vulnerability)

![[cgi_scanner_success.png]]

Now that the scanner was successful, try the exploit

![[apache_fail.png]]

But the exploit fails then I looked at the other services


The web server running on port 8000 is strange, so I searched on Metasploit for `Werkzeug` and found an RCE exploit

![[werkzeug_exploit.png]]

But this exploit didn't work.