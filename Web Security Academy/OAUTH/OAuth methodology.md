# OAuth methodology

# 1. Identify OAuth

Confirm that the service is being used. Use Burp Proxy to identify a request to an OAuth service.

# 2. Recon

Perform basic recon of the service by looking for the `hostname` for the service provider and make a GET request to the following standard endpoints

-   `/.well-known/oauth-authorization-server`
-   `/.well-known/openid-configuration`

Look for: Details for additional features not mentioned on the documentation.

# Testing

Test for these common vulnerabilities

- Vulnerabilities in the client application
	-  [[Improper implementation of the implicit grant type]] more info [here](https://portswigger.net/web-security/oauth#improper-implementation-of-the-implicit-grant-type) 
	- [Flawed CSRF protection](https://portswigger.net/web-security/oauth#flawed-csrf-protection)
- Vulnerabilities in the OAuth service
	- [Leaking authorization codes and access tokens](https://portswigger.net/web-security/oauth#leaking-authorization-codes-and-access-tokens) 
	- [Flawed scope validation](https://portswigger.net/web-security/oauth#flawed-scope-validation)
	- [Unverified user registration](https://portswigger.net/web-security/oauth#unverified-user-registration)
