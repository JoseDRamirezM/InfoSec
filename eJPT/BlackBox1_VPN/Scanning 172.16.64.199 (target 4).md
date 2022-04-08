# Scanning 172.16.64.199 (target 4)

Scanning the host with nmap

![[target4_ports.png]]

OS Detection failed but looking at the open ports it's probable that the machine is running some version of Windows.

Now fingerprint the services.

![[target4_services_1.png]]

![[target4_services_2.png]]

From the service fingerprint output I can tell the machine is running Windows 10.