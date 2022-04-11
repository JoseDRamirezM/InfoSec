# Information gathering pivoted network

Now that I performed pivoting let's scan the network running the **auxiliary/scanner/portscan/tcp** module and configure it as follows:

![[pivoted_portscan.png]]

The hosts are specified by a range in this case **1-10** , also configure the range of ports if necessary as it takes a while for the scan to complete, next run the module.

![[pivoted_portscan_result.png]]

There are a lot of ports open on `192.148.151.3` that is other host on the pivoted network.

I tried to forward the open ports and try to fingerprint the services but the scan was blocked by TCP wraps. The lab solution has the correct way to access the resources on the other network.

# Using the Meterpreter as a SOCKS PROXY
Use the  `auxiliary.server/socks_proxy`  module.

![[SOCKS_pproxy.png]]

Configure and run

![[SOCKS_conf.png]]

The `-j` flag makes the process to run in the background.

Then scan the host with a TCP Connect() scan (-sT flag on Nmap) otherwise the scan will not show the running services.

![[pivoted_nmap_scan.png]]

The above command generates the following output.

![[jenkins.png]]

Now I know there's a web application running on a Jetty server.

# Configure browser to use the SOCKS proxy server

In order to fully interact with the service on port 8080 the attacker's browser must be configured to reach and retrieve information.

![[browser_socks_config.png]]

The access the resource normally 
![[resource_reachable.png]]

Now let's see how to exploit Jenkins.

![[Exploit Jenkinks]]
