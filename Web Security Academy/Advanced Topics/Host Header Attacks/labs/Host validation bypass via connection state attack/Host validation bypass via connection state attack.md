This lab is vulnerable to routing-based [SSRF](https://portswigger.net/web-security/ssrf) via the Host header. Although the front-end server may initially appear to perform robust validation of the Host header, it makes assumptions about all requests on a connection based on the first request it receives.

To solve the lab, exploit this behavior to access an internal admin panel located at `192.168.0.1/admin`, then delete the user `carlos`.

# Vuln assessment

The server is reusing connections by using the `Connection: keep-alive` header, causing each connection to have a timeout reflected on the `Keep-Alive: timeout=10` header.

When the connection times out, the client will initiate a new connection with the server where the `Host` header will be thoroughly validated. This allows to perform SSRF quite easily by simple changing the Host header.

# Exploitation

Burp Suite allows to send these requests on a single connection in one of its features:

1. Create a tab group with a regular request to the home page and other with the `/admin` path and the injected Host header `192.168.0.1`
2. The send button will not have multiple options, select:

![[single-connection.png]]

3. Send the requests with this option and note that the admin panel is successfully requested:

![[Advanced Topics/Host Header Attacks/labs/Host validation bypass via connection state attack/images/admin-panel.png]]

4. Send the corresponding request to delete the user using the same approach

![[Advanced Topics/Host Header Attacks/labs/Host validation bypass via connection state attack/images/lab-solved.png]]