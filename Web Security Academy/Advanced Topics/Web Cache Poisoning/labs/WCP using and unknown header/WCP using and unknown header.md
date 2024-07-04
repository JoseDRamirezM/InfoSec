This lab is vulnerable to web cache poisoning. A victim user will view any comments that you post. To solve this lab, you need to poison the cache with a response that executes `alert(document.cookie)` in the visitor's browser. However, you also need to make sure that the response is served to the specific subset of users to which the intended victim belongs.

# Recon

As in previous labs it's necessary to check the application resources, this time regarding a script related to the comments functionality.

![[Advanced Topics/Web Cache Poisoning/labs/WCP using and unknown header/images/entrypoint.png]]

That didn't seem to be the entry point for the attack, I used param miner on the requests made when accessing a post and found the entry point:

![[cache-poison.png]]

# Vuln assessment

1. Find the request to poison

Now craft an appropriate payload to execute the desired action and post a comment to that particular post, to make the user check the "comments" and deliver the malicious cached response.

![[header-injected.png]]

Now the problem is getting the user to view the malicious cached page, inspect how the comments functionality works:

2. Set up the exploit server

Insert the `alert(document.cookie)` payload matching the file path that the server uses:

![[exploit-server-setup.png]]


3. The attack requires finding out the target's User-Agent

Doing this require inserting a simple `img` HTML tag on the content so that, when the target user checks the comment the User-Agent is logged on the exploit server

```
<img src="exploit-server.com" />
```


Checking the server's logs I found the target's User-Agent

![[victim-user-agent.png]]


![[vary-header.png]]

The `Vary` header is also present, this is used to target the right subset of users.


3. Poison the cache for the target User-Agent

![[Advanced Topics/Web Cache Poisoning/labs/WCP using and unknown header/images/exploited.png]]