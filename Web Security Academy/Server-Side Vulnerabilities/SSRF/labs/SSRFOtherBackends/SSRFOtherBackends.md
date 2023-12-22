# SSRFOtherBackends
#WRITEUP <hr>
## Recon

The same exploitation process from the previous lab is also applied here, the difference is that now I had to "scan" for a valid IP address in order to access the admin panel, injecting the payload `http://192.168.0.X/admin`.

## Vulnerability assessment

Using Burp intruder it's easy to try all the possible IP addresses until the right one is found.

![[Pasted image 20230505155955.png]]

After the attack is executed, one of the IP addresses returned a 200 status code.

![[Pasted image 20230505160203.png]]

## Exploitation

Inspect the response and the admin panel appears.

![[Pasted image 20230505160250.png]]

Lastly, delete user carlos by placing the following payload for the stock check functionality:

`http://192.168.0.238:8080/admin/delete?username=carlos`

