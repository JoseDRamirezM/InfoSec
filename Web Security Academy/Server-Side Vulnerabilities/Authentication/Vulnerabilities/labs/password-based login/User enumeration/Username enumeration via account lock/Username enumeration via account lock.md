# Username enumeration via account lock
#AUTHENTICATION 
#WRITEUP 

## Enumerate the valid user

For this lab the community edition of Burp Suite is useless, so I wrote a python script to make five attempts on each user looking for differences in the response. I found that the `azureuser` account was blocked after the failed attempts.

Check the script [here](https://github.com/JoseDRamirezM/InfoSec/blob/main/Web%20Security%20Academy/Authentication/Vulnerabilities/labs/password-based%20login/User%20enumeration/Username%20enumeration%20via%20account%20lock/exploit.py)

Next Perform an Sniper attack on the found user password. The correct password can be recognized as even though the account is blocked the response does not contain any error message.

![[correct.png]]

Wait for the account to unlock if it is the case, log in and the lab is solved.