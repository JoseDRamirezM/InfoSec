# Blind SQL injection with conditional responses
#BLINDSQLI 
#WRITEUP 

For this lab `Burp Intruder` may not be the best strategy, I wrote a Python script to automate the process of sending each letter and incrementally construct the password string. This can be done on `Burp Intruder` but it will be very time consuming.

	Note: I realized maybe it can be done faster by using the Burp's Turbo Intruder extension.

## The script

![[result.png]]

The above image corresponds to the function that makes the heavy lifting in terms of determining if the character correspond to the given index, by looking for the `Welcome Back` message on the page as an indication that the tested character corresponds to the given index and return said character.

Then a string accumulates the characters until no character receives a positive response which means the password is complete. The output indicates the index that's been tested and the progress so far. Once it's finished login as the `administrator` user and the lab is complete!

![[SQLInjection/Attacks/Blind SQL injection/labs/Blind SQL injection with conditional responses/images/password.png]]
The script is available [here](https://github.com/JoseDRamirezM/InfoSec/blob/main/Web%20Security%20Academy/SQL%20injection/Attacks/Blind%20SQL%20injection/labs/Blind%20SQL%20injection%20with%20conditional%20responses/get_pass.py)


