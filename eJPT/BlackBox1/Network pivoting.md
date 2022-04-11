# Pivoting using a Meterpreter session

Use the autoroute command to add a route to the compromised target unreachable network.

![[autoroute.png]]

Check the network IP of the unreachable network

![[add_route.png]]

The route is created.

## Perform a port scan on the network

Now that the network is accessible and the compromised machine doesn't have nmap installed, run a port scan with Metasploit.

Search for the correct portscan module

![[portscan_module.png]]

Configure the module and star the scan

![[portscan_module_config.png]]

![[portscan_result.png]]

## Port forwarding

Once the interesting ports are discovered, it's possible to forward communication from the unreachable network to a local port.

### portfwd

Use the portfwd command on the open Meterpreter session.

![[portfwd_help.png]]

Forward the port 21 (FTP) to local port 5678

![[portfwd_success.png]]

Now scan the target with nmap

### Pivoted host nmap scan

![[fwdport_scan_success.png]]

Search for exploits for that service

![[FTP_service_exploits.png]]

![[FTP_metasploit_exploit.png]]

Configure and exploit

![[ftp_exploit_config.png]]

![[ftp_exploit_worked.png]]

Then explore the host and capture the flag

![[flag_2.png]]

THE END