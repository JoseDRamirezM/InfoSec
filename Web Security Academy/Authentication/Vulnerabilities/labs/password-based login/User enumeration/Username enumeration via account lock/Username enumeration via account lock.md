# Username enumeration via account lock

## Enumerate the valid user

For this lab the community edition of Burp Suite is useless, so I wrote a python script to make five attempts on each user looking for differences in the response. I found that the `azureuser` account was blocked after the failed attempts.

Next Perform an Sniper attack on the found user password. The correct password can be recognized as even though the account is blocked the response does not contain any error message.

