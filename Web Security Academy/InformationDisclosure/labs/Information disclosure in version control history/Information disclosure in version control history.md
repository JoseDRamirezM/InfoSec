# Information disclosure in version control history

#WRITEUP 
#INFORMATIONDISCLOSURE 

<hr>

## Recon

This lab discloses sensitive information via its version control history. To solve the lab, obtain the password for the `administrator` user then log in and delete Carlos's account.

## Vulnerability assessment

Search for the version control directory.

It was quite easy as it was in the `/.git` endpoint, next search for the `administrator` password.

Next download all the contents from the .git directory using this command:

`wget lab.url/.git -r`

## Exploitation

Once obtained check the commits information

![[commit.png]]

![[commit-local.png]]

Then get the changes made between the commits using `git diff 3c6c9f 9fdd5b`

![[admin-pass.png]]

Then login as the administrator user delete Carlo's account and the lab is solved.

