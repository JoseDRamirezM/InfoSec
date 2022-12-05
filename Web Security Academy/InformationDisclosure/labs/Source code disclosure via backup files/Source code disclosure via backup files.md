
#WRITEUP 
#INFORMATIONDISCLOSURE 

<hr>

## Vulnerability assessment

This application contains a hidden directory which contains a backup of the source code.

I checked if the `robots.txt` file was available.

`https://lab-url/robots.txt`

![[InformationDisclosure/labs/Source code disclosure via backup files/images/robots.png]]

I went to the directory and I found the source code backup.

![[backup-folder.png]]

## Exploitation

Analyze the content of the backup file and check for the database password.

![[SAST.png]]

Submit the database password and the lab is solved.

