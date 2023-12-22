# Improper implementation of the implicit grant type

Due to how the [[Implicit grant type]] works, sending the access token via the browser this grant type is recommended for single-page applications but is often used on client-server web applications because of its simplicity.

The vulnerability takes place when the application wants to maintain the user session, it needs to store the current user data (user ID and access token).

To solve this problem the client application submit the data to the server on a `POST` request and assign the user a <font color=red>session cookie</font> (logging the user in). But the server implicitly trust the data sent on that request, which is exposed to attackers via their browser. This can lead to a serious vulnerability if the server doesn't properly check that the <font color=yellow>access token</font> corresponds to the data sent in the request. An attacker could change the parameters to impersonate any user.

[[LAB Improper implementation of the implicit grant type ]]