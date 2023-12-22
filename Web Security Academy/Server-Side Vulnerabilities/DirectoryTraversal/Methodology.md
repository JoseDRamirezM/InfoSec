# Methodology
#METHODOLOGY 
#DIRECTORYTRAVERSAL 
<hr>

Test parameters that retrieve content like images from the server, based on the file name.

1. Try to use `Traversal sequences` like `../../` to retrieve a system file like:
- `/etc/passwd`
- `\windows\win.ini`

2. Try using an absolute path to a system file.

3. Try using nested traversal sequences, like:
- `....//`
- `....\/`

4. Try using encoded traversal sequences
	- URL encoding
		- `../` -->  `%2e%2e%2f`
	- Double URL encoding
		- `../` --> `%252e%252e%252f`
	- Non-standard encoding
		- `../` --> `..%c0%af`
		- `../` --> `..%ef%bc%8f`

5. Check if a base folder is expected in the file path, from there insert the suiting traversal sequences to reach the target folder.

`filename=/var/www/images/../../../etc/passwd`

6. If the application expects the file path to end with a file extension try using a null byte `%00` to terminate the file path and then provide the required file extension.

`filename=../../../etc/passwd%00.png`