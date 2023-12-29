# Port scan

![[ports.png]]

![[Pasted image 20231216124137.png]]

# Port 22

...

# Port 80

## dev.devvortex.htb

### Subdomain enumeration

![[subdomain-enum.png]]

``` bash
wfuzz -c -f sub-fighter -w ~/tools/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://devvortex.htb" -H "Host: FUZZ.devvortex.htb" --hc 302
```

The `dev.devvortex.htb` subdomain is found.

### Files & directories enumeration

![[dirs.png]]

Interesting directories:
- `/administrator`
- `/api`

