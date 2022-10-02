# Authentication bypass via encryption oracle
#WRITEUP 
#LOGICFLAWS 
<hr>

## Vulnerability assessment

The blog application sends an encrypted `notification` cookie when a user provides invalid input.


![[Pasted image 20221001163037.png]]

![[Pasted image 20221001163157.png]]

![[Pasted image 20221001163222.png]]

Try to put the stay logged in cookie in the notification cookie, to see if the application outputs clear text of the stay logged  in cookie.

![[Pasted image 20221001163411.png]]

![[Pasted image 20221001163532.png]]

The application decodes the stay logged in cookie, next figure out what those numbers are.

I figured out that it was an UNIX timestamp with the date and time that the user logged in.

![[Pasted image 20221001163736.png]]

Now the question is: How can this be abused?

Basically there's a way to encrypt and decrypt data with the notification cookie. Providing an invalid email will encrypt user supplied data and also print it in clear text.

The only thing that interferes with the exploitation is that there's an unwanted string `Invalid email address: ` in the notification cookie. For that strip those bytes using Burp Decoder.


### Payload construction

Take the encrypted payload (cookie) and follow these steps:

1. URL decode.
2. Base-64 decode.
3. Delete the first 23 bytes.

Submit the cookie to check the output.

![[error.png]]

The thing is that the deleted bytes must 

7JMagw/pIOLHSI6ybdm+XQfdTf9nkHW2Mb6ZGMlXP4AkhXfIBz+/NqQOmopd6c6TAxBXLTwuwBAV5QqjhgRspA==

7JMagw/pIOLHSI6ybdm+XVjU02/Rp3faaYOQgTREgk4=