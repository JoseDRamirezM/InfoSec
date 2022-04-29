# Authorization code grant type

Once the OAuth flow is started by the first stage the client application obtains the <font color=red>authorization code</font> and exchanges it with the OAuth service to get an <font color=red>access token</font> to make the API calls.

This process is made <font color=yellow>server to server</font> over a secure channel that is invisible to the end user. The client application uses the <font color=red>client_secret</font > to authenticate in the <font color=yellow>server to server</font> communication.

This grant type is secure. Server-side applications should use this grant type.

![[oauth_process.png]]


## OAuth flow for the authorization grant type

### 1. Authorization request

The client application sends a request to the OAuth service `/authorization` endpoint. The authorization endpoint may vary between providers, but it can be identified via the request.


```
GET /authorization?client_id=12345&redirect_uri=https://client-app.com/callback&response_type=code&scope=openid%20profile&state=ae13d489bd00e3c24 HTTP/1.1 
Host: oauth-authorization-server.com
```

#### Request parameters

- `client_id` : Mandatory parameter that contains the identifier for the client application, it's generated when the application registers with the OAuth service.
- `redirect_uri` :  The URI where the user's browser should be redirected when sending the authorization code to the client application. Also called <font color=green>callback URI</font> or <font color=green>callback endpoint</font>. Most OAuth attacks are based on exploiting flaws on the validation of this parameter.
- `response_type` : Specifies the type of response the client application is expecting and which flow it wants to initiate. For the <font color=yellow>authorization grant type</font> the value should be `code`.
- `scope` : Specifies the subset of user data that the client application wants to access. The scope can be custom or standardized by the <font color=red>OpenID connect specification</font>.
- `state` : Stores a unique unguessable value tied to the current session. The OAuth service should respond with the same value along with the <font color=yellow>authorization code</font>. It serves a function similar to a <font color=red>CSRF token</font> it validates that the requests made to the `/callback` endpoint (defined on the `redirect_uri` parameter) is the same person that initiated the <font color=yellow>OAuth flow</font>.

### 2. User login and consent

The user selects an account to log in with the OAuth provider. Then information about the list of data that the client application wants to access is presented. The user has to choice to consent this or not.

Once this process is done, it will not be repeated as long as the user has a valid session with the OAuth service. Allowing to log in with a single click.

### 3. Authorization code grant

Once the user grants permission the browser will be redirected to the `/callback` endpoint. The resulting `GET` request will contain the authorization code as a query parameter and depending on the configuration the `state` parameter.

```
GET /callback?code=a1b2c3d4e5f6g7h8&state=ae13d489bd00e3c24 HTTP/1.1 Host: client-app.com
```

### 4. Access token request

On this step the <font color=yellow>Authorization code</font> is exchanged for the <font color=yellow>access token</font> via a `POST` request to the OAuth service `/token` endpoint. From this point forward the communication is made on a back-channel hence it reduces the chances for it to be controlled by and attacker.

```
POST /token HTTP/1.1 Host: oauth-authorization-server.com … 

client_id=12345&client_secret=SECRET&redirect_uri=https://client-app.com/callback&grant_type=authorization_code&code=a1b2c3d4e5f6g7h8
```

The `client_secret` and `grant_type` parameters are sent also.

### 5. Access token grant

Validations are made to the request made on the previous step and if it succeeds the server responds with the <font color=yellow>access token</font> with the requested <font color=yellow>scope</font>.

![[access_token.png]]

### 6. API call

Now the client application fetch the user data making API calls to the `/userinfo` endpoint. The access token is used on the `Authorization : Bearer` header.

![[API_call.png]]


### 7. Resource grant

The token is validated for the current client application, to finally retrieve the requested user data based on the scope for the access token.

![[user_data.png]]

The client application typically uses the data to authenticate the user.