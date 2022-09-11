# Inconsistent handling of exceptional input
#LOGICFLAWS 
#WRITEUP 
<hr>

## Recon

The lab states the vulnerability resides in the registration process, inspect this functionality.

![[form.png]]

The message can be a hint. Use the `admin@dontwannacry.com` email?

When visiting the `/admin` endpoint, it contains the following message:

![[more_hints.png]]

So the goal is to successfully register as a `XYZ@dontwannacry.com` user.

I tried to treat the `@dontwannacry.com` as a subdomain of the email client domain. To see if maybe the app only checked that the email contains the `dontwannacry` string.

## Exploitation

The thing with this lab is that when a very large email is provided, it is truncated to 255 characters.

![[evil_req.png]]

![[truncatedemail.png]]

Taking advantage of this it's possible to create an user that has the `@dontwannacry.com`  domain and still receive the registration email in the attacker controlled server.

For that my approach was:

1. Use a character count tool
2. Paste `@dontwannacry.com` and add the necessary characters so that:
	- `CHARS-HERE@dontwannacry.com` is 255 characters in length.

![[BusinessLogic/labs/Inconsistent-handling-of-exceptional-input/images/payload.png]]
3. Then append the attacker controlled domain to receive the registration email

![[payload_1.png]]

5. Use the email above to register an account.

![[BusinessLogic/labs/Inconsistent-handling-of-exceptional-input/images/exploited.png]]

Now access the admin panel and delete the user Carlos.