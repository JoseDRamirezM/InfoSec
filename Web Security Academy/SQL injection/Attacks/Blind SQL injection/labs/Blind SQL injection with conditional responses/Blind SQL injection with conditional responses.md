# Blind SQL injection with conditional responses

For this lab `Burp Intruder` may not be the best strategy, I wrote a Python script to automate the process of sending each letter and incrementally construct the password string. This can be done on `Burp Intruder` but it will be very time consuming.

## The script

![[result.png]]

The above image corresponds to the function that makes the heavy lifting in terms of determining if the character correspond to the given index, by looking for the `Welcome Back` message as an indication that the tested character corresponds to the given index and return said character.

Then a string accumulates the characters until no character receives a positive response which means the password is complete.

The output indicates the index that is been tested and the progress so far.




