# Blind OS command injection with output redirection
#COMMANDINJECTION 
#WRITEUP 
<hr>

## Recon

The writable file in the server is `/var/www/images` then explore the application logic to retrieve images to figure out the URL to  get the output redirection file of the `whoami` command. Also the `feedback` functionality is vulnerable.


1. Figure out how the application retrieves images.

![[frontend.png]]

Then check the requests that are made.

![[Pasted image 20220827145706.png]]

Following this logic, there's a file `4.jpg` in the `/var/www/images` directory, specified by the `filename` GET parameter.

2. Find the injection point

Test the parameters in the `Submit feedback` form.

![[injected_req.png]]

Then go to `/image?filename=whoami.txt`.

![[labs/Blind OS command injection with output redirection/images/exploited.png]]

The command executed successfully and it was possible to retrieve the file.