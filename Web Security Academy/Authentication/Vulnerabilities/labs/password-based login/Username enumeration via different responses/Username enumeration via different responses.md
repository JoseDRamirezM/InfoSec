# Username enumeration via different responses

1. Enumerate the user

Provided with the username wordlist use Burp's `Intruder` to automate the requests.

![[intruder.png]]

Now look at the responses searching for differences in the response

![[user.png]]

The valid user `al` is found. Repeat the process but now testing the password.

2. Dictionary attack on password

As the page diplays the message `Incorrect password` apply a filter with the word `Incorrect` and check the result.

![[pass.png]]

A database record matches the credentials and a `302 Found` status code is returned, so the credentials are `al:amanda`.

Log in and the lab is solved!