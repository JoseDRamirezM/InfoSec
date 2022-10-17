# Directory Traversal

#THEORY 
#DIRECTORYTRAVERSAL
<hr>

## Base scenario

Also known as file path traversal is a web security vulnerability that allows an attacker to read arbitrary files on the server that is running the application. Often sensitive information like source code, passwords and OS files. Some times it is even possible to write files to the server which may allow to modify data (affect integrity) or take full control of the server.

Consider a shopping application that displays images of items for sale. Images are loaded via some HTML like the following:

`<img src="/loadImage?filename=218.png">`

The `loadImage` URL takes a `filename` parameter and returns the contents of the specified file. The image files themselves are stored on disk in the location `/var/www/images/`. To return an image, the application appends the requested filename to this base directory and uses a filesystem API to read the contents of the file. In the above case, the application reads from the following file path:

`/var/www/images/218.png`

The application implements no defenses against directory traversal attacks, so an attacker can request the following URL to retrieve an arbitrary file from the server's filesystem:

`https://insecure-website.com/loadImage?filename=../../../etc/passwd`

This causes the application to read from the following file path:

`/var/www/images/../../../etc/passwd`

The sequence `../` is valid within a file path, and means to step up one level in the directory structure. The three consecutive `../` sequences step up from `/var/www/images/` to the filesystem root, and so the file that is actually read is:

`/etc/passwd`

On Unix-based operating systems, this is a standard file containing details of the users that are registered on the server.

On Windows, both `../` and `..\` are valid directory traversal sequences, and an equivalent attack to retrieve a standard operating system file would be:

`https://insecure-website.com/loadImage?filename=..\..\..\windows\win.ini`

#### Exploitation example

[[File path traversal simple case]]


<hr>

## Bypassing common protections

### Absolute path reference to a file

Use an absolute path to an specific file, without using any traversal sequences.

```HTTP
example?filename=/etc/passwd
```

#### Exploitation example

[[File path traversal, traversal sequences blocked with absolute path bypass]]

### Stripping traversal sequences

It may be possible to use nested traversal sequences, like:
- `....//`
- `....\/`

If the code strips these sequences non-recursively the result path will contain traversal sequences.


#### Exploitation example

[[File path traversal, traversal sequences stripped non-recursively]]


### URL decode file path

The URL path of a `filename` parameter of a `multipart/form-data` request the server may strip traversal sequences before passing the value as input to the application. To bypass this try these techniques with traversal sequences `../`:

1. URL encoding
	- `../` -->  `%2e%2e%2f`
2. Double URL encoding
	- `../` --> `%252e%252e%252f`
3. Non-standard encoding
	- `../` --> `..%c0%af`
	- `../` --> `..%ef%bc%8f`

#### Exploitation example

[[File path traversal ]]
### Start of path validation

If the application validates that the provided filename starts with the expected base folder e.g `/var/www/images`, it may be possible to retrieve an arbitrary file by providing the base folder followed by the  suitable traversal sequences.

```
filename=/var/www/images/../../../etc/passwd
```

#### Exploitation example

[[File path traversal, validation of start of path]]


### Expected file extension

If the application validates that the user-supplied filename ends with an expected file extension e.g (png, jpeg, jpg) try using a null byte to terminate the file path before providing the required file extension.

`filename=../../../etc/passwd%00.png`

#### Exploitation example

[[File path traversal, validation of file extension with null byte bypass]]


## How to prevent a directory traversal attack

Avoid passing user-supplied input to file system APIs. Many functionalities can be re-written to deliver the same behavior in a safer way.

If doing so is unavoidable implement two layers of defense:

1. Perform proper input validation, ideally use a whitelist of permitted values. Ultimately verify that the input contains only permitted content like alphanumeric characters only.
2. Use a platform file system API to `canonicalize` the path i.e normalize the path representation of the file, then compare that the canonical path starts with the expected base directory.

Java example code

```Java
File file = new File(BASE_DIRECTORY, userInput); if (file.getCanonicalPath().startsWith(BASE_DIRECTORY)) { 
	// process file 
}
```