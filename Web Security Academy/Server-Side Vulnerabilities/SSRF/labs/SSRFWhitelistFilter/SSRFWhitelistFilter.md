# SSRFWhitelistFilter
#WRITEUP <hr>
## Recon

Basic testing of SSRF gives a hint about the host to be used.

![[hint.png]]

## Vulnerability assessment

Try to bypass the filter by manipulating the input.

![[first.png]]

The payload above will connect to the regular service. Now try to manipulate it further to request to `http://localhost`

![[SSRF/labs/SSRFWhitelistFilter/images/payload.png]]

Double URL encoding the character `#` allowed to ignore the rest of the expected domain, after it.

`http://localhost%2523@stock.weliketoshop.net:8080/`

## Exploitation

Now access the admin panel at:

`http://localhost%2523@stock.weliketoshop.net:8080/admin`

![[deletePanel.png]]

Then extract the delete URL for user `carlos` from the response and issue the request.

