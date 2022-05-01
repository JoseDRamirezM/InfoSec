# Implicit grant type

This grant type is simpler. It skips a few steps by granting the <font color=yellow>access token</font> one the user consents the access to his information.

Compared to the [[Authorization code grant type]] this grant type is less secure. All communications are no longer made via a back-channel instead made via browser redirects, so user data is more exposed to potential attacks.

This grant type suits single page applications and native desktop applications. As storing the `client_secret` on the backend is not that easy.

![[implicit_flow.png]]

## OAuth flow for the implicit grant type

### 1. Authorization request

The flow starts almost the same as the [[Authorization code grant type]], in this case the `response_type` is set to `token`.

```
GET /authorization?client_id=12345&redirect_uri=https://client-app.com/callback&response_type=token&scope=openid%20profile&state=ae13d489bd00e3c24 HTTP/1.1 
Host: oauth-authorization-server.com
```


### 2. User login and consent

The user is asked to grant the requested permissions.

### 3. Access token grant

Here's where the process changes. The OAuth service redirects the user browser to the `redirect_uri` specified in the authorization request. The service now sends the access token along with other related information on the URL.

```
GET /callback#access_token=z0y9x8w7v6u5&token_type=Bearer&expires_in=5000&scope=openid%20profile&state=ae13d489bd00e3c24 HTTP/1.1 
Host: client-app.com
```

The access token is not sent to the client application directly, this creates the need for a suitable script that extracts and stores the token from the URL.

### 4. API call

Once the <font color=yellow>access token</font> is obtained the client application can perform API calls to the `/userinfo` endpoint via the browser.

![[implicit_api_call.png]]

### 5. Resource grant

The resource server validates the token with the current client application and retrieves the user data based on the  <font color=yellow>scope</font> for the access token.

Finally the client application typically uses the obtained data to authenticate the user.





