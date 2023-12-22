# basicSSRF
#WRITEUP <hr>
## Recon

The lab hints about checking the products stock in the page and requesting `http://localhost/admin`.

![[Pasted image 20230505150956.png]]

After changing the parameter, the following appears:

![[Pasted image 20230505151136.png]]

![[Pasted image 20230505151216.png]]



## Vulnerability assessment

The previous image shows that there's a SSRF vulnerability, the app will only allow to perform requests to the local service and delete users if the requests comes from an internal IP or loopback.

## Exploitation

Following the previous explanation it's now a matter of requesting the right endpoint to delete user carlos.

![[Pasted image 20230505152206.png]]

