# OAuth authentication vulnerabilities

## How do vulnerabilities on OAuth arise?

There's a lot of room for bad practice when implementing the OAuth services, the specification is vague and flexible by design. Many configuration settings for user data security are optional.

Also there's a lack of built-in security features, the developers have to deal with this and with any additional measure. Depending on the grant type, sensitive data is sent over the browser making it possible for an attacker to intercept it.

## Identifying OAuth authentication

If an application has an option for users to log in with social media, there's a great chance that OAuth is being used.

### Methodology

1. Use Burp Proxy to intercept the first request to OAuth service, it should be to the `/authorization` or `/auth` endpoint containing the query parameters corresponding to OAuth flows for [[OAuth grant types]].
2. Look for the `client_id`, `redirect_uri` and `response_type` parameters.

Typically it looks as follows:

![[init_request.png]]

# Recon

To widen the attack surface and to identify vulnerabilities perform basic recon on the OAuth service.

1. Identify the OAuth provider based on the `hostname` to which the authorization request is sent. Providers has an open API which may contain useful information and detailed documentation about endpoints and configuration options.
2. Once the `hostname` is obtained make a GET request to the following standard endpoints.

	- `/.well-known/oauth-authorization-server`
	- `/.well-known/openid-configuration`

Which may return a JSON configuration file containing useful information.

[[Exploiting OAuth authentication vulnerabilities]]
