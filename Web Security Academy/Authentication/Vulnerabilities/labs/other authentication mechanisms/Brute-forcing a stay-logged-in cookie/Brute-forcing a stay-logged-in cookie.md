# Brute-forcing a stay-logged-in cookie

#WRITEUP 
#AUTHENTICATION 

## Recon

Analyze the generated cookie when the Stay logged-in functionality is enabled.

![[login.png]]

![[cookie.png]]

## Analyze cookie

Try to know if the cookie is encoded or encrypted somehow.

![[cookie_encoded.png]]

The cookie is `Base64` encoded and uses `username:hash`, analyzing the hash it may be an `MD5` algorithm. Then I tried to crack this with online tools.

I used [CrackStation](https://crackstation.net/)

![[hash.png]]

So the cookie's structure is

```
base64(username:MD5(password))
```

## Brute-force the cookie to get access to carlos account

Use Burp Intruder with the `GET` request to the `/my-account` endpoint, placing the payload indicator in the `stay-logged-in` cookie value. As I showed before the cookie value requires payload processing to achieve the desired result.

![[processing.png]]

Load all candidate passwords and apply the processing rules showed above.

Start the attack .

Something weird happened with this lab, as making the requests to the endpoint `/my-account` didn't work, because I didn't log out from the known user session.

So I requested for the `/` endpoint and filtered the responses to contain the word `carlos`.

![[Vulnerabilities/labs/other authentication mechanisms/Brute-forcing a stay-logged-in cookie/images/success.png]]

Now crack the user's password.

![[Vulnerabilities/labs/other authentication mechanisms/Brute-forcing a stay-logged-in cookie/images/carlos_pass.png]]
