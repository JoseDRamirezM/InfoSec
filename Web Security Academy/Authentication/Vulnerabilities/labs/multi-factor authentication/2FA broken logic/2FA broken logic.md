# 2FA broken logic

#AUTHENTICATION 
#WRITEUP 

## Recon

Try to login with the provided `wiener` user credentials and check the email server present on the website to receive the verification code.

![[recon.png]]

After submitting the credentials an email containing the verification code is received.

![[email_client.png]]

With that in mind check the requests on each step.

## Requests analysis

- Login first step

Request

![[first_step.png]]

Response

![[second_step.png]]

It describes the same scenario as the material, so FIRST request send a `GET` request to `/login2` changing the `verify` cookie value to `carlos`. Then brute force the verification code again changing the cookie value to `carlos`.

As I don't have Burp Suite Professional I managed to do it with `OWASP ZAP`.

- Trigger the verification code generation

![[trigger.png]]

- Brute force the verification code

First send the `POST` request again to `/login2` changing the `verify` cookie value

![[correct_req.png]]

- Brute force the verification code

Using ZAP's Fuzzer define the correct payload `0000-9999` and start the attack. Look for a `302 Found` status code and you'll know the corresponding verification code.

![[payload_gen.png]]

Define the right processor to match the payload requirements.

![[process_payloads.png]]


Start fuzzing and find the correct verification code.

![[code.png]]

Then resend the request and check the response.

![[Vulnerabilities/labs/multi-factor authentication/2FA broken logic/images/success.png]]

The lab is solved!