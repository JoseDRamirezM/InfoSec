# Information disclosure vulnerabilities
#THEORY 
#INFORMATIONDISCLOSURE 
<hr>

## What is information disclosure?

A.k.a information leakage occurs when a website unintentionally reveals sensitive information to its users.

Information like:

-   Data about other users, such as usernames or financial information
-   Sensitive commercial or business data
-   Technical details about the website and its infrastructure

The application may leak information in two scenarios:

- Regular user interaction with the application
- Malicious user interaction with the application

### What are some examples of information disclosure?

Some basic examples of information disclosure are as follows:

-   Revealing the names of hidden directories, their structure, and their contents via a `robots.txt` file or directory listing
-   Providing access to source code files via temporary backups
-   Explicitly mentioning database table or column names in error messages
-   Unnecessarily exposing highly sensitive information, such as credit card details
-   Hard-coding API keys, IP addresses, database credentials, and so on in the source code
-   Hinting at the existence or absence of resources, usernames, and so on via subtle differences in application behavior

