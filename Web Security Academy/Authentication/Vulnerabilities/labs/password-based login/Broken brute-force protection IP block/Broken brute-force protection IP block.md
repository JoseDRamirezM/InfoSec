# Broken brute-force protection IP block
#AUTHENTICATION 
#WRITEUP

## Recon

The lab implements the IP block protection, in a plain `Intruder` sniper attack against the password of the user `carlos`.

After three failed attempt a one minute timeout that won't allow me to keep sending login requests.

![[IP_block.png]]

To solve that I tried to create two wordlists of both usernames (carlos username repeated many times) and passwords in which the provided credentials `wiener:peter` were every three lines (or attempts) hoping to reset the failed attempt counter.

## Custom wordlist

The solution didn't work so I tried to change the interval to two login attempts and the timeout was not triggered. For that purpose I wrote a bash script to automate a little (not very flexible script though).

Change to a `Forksplit` attack and provide both payload sets. After waiting for a bit the `carlos` user password is found.

![[carlos_pass.png]]


Log in with `carlos:11111111` and the lab is solved.