# Username enumeration via response timing
#AUTHENTICATION 
#WRITEUP 

## Recon

Noticing the goal of the lab I started an Intruder attack providing the list of usernames and a long password to make the time delays evident.

I added the `Response received` and `Response completed` columns to the attack and sorted the request based on the `Request completed` looking for the highest value.

![[time_1.png]]

Even though looking at the response message and the lab's hint an IP-based brute force protection is implemented, which limits the number of request that an specific IP can make in a period of time.

I looked for a way to bypass this and I found [this](https://medium.com/r3d-buck3t/bypass-ip-restrictions-with-burp-suite-fb4c72ec8e9c) which explained clearly the bypass method.

## Protection bypass
#IPBYPASS

Basically using the `X-Forwarded-From` HTTP header it is possible to make as many request as needed for the attack. The header tricks the application by providing in this case a loopback IP address to avoid the server to block the requests.

![[Server-Side Vulnerabilities/Authentication/Vulnerabilities/labs/password-based login/User enumeration/Username enumeration via response timing/images/bypass.png]]

## Pitchfork attack
#MULTIPLEPAYLOADS

Despite the fact that this was the correct way, it failed because the IP address had to be changed in every request or at least every 4 login tries (which is not possible in Burp). So I learned about other type of attack of the `Intruder` called `Pitchfork` which allowed multiple payload sets.

Define the login request as follows

![[login_req.png]]

It's important to provide a long password as it will make the delay evident if the username is valid.

Then configure the payload sets as follows:

- IP address payload

![[IP_payload.png]]

Valid `127.0.X.1` loopback IP addresses (I think any range of valid IP addresses work).

- Usernames payload

Load the username word list.

## Launch the attack!

After it's finished add the appropriate columns to analyze the response time and look for the highest value.

![[highest.png]]

The `announce` user is candidate to be valid.

## Brute force the user password

Define the request and the payloads once more.

![[brute_req.png]]

Launch the attack!

![[user_password.png]]

A `302 Found` status code means the resource was found (database records matched) for the provided credentials.

Login with `announce:dallas` credentials and the lab is solved.

