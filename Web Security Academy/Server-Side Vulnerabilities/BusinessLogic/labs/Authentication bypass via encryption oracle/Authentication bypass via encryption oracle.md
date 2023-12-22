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

Basically the request to post a comment is used to encrypt data and the request of a blog post that contains the `notification` cookie is used to decrypt data. Providing an invalid email will encrypt user supplied data and also print it in clear text once the blog post is requested again.

The only thing that interferes with the exploitation is that there's an unwanted string `Invalid email address: ` in the notification cookie. For that strip those bytes using Burp Decoder.

### Payload construction

Take the encrypted payload (cookie) and follow these steps:

1. URL decode.
2. Base-64 decode.
3. Add 9 characters to the payload i.e `xxxxxxxxxadministrator:timestamp`. This is done to effectively removing the part of the cookie that reads: "`Invalid email address:`" adding a 9 character padding to sum up 32 bytes to be removed. Doing this will prevent the block decryption algorithm to fail.
4. Delete the first 32 bytes.
5. Rencode (Base64 and URL) and submit the cookie to check the output.

![[cookie-working.png]]

5. Remove the session cookie and replace the `stay-logged-in` cookie with the crafted payload

Once the request is issued the Admin panel should appear:

![[cookie-worked.png]]

Access the admin panel and delete user carlos:

![[fin.png]]

