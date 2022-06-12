# Blind SQL injection with time delays
#BLINDSQLI 
#WRITEUP 

Looking at the payloads available on the [SQL injection cheatsheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
![[payload.png]]

I tried the PostgreSQL payload and it worked.

```SQL
';SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg_sleep(10) ELSE pg_sleep(0) END--
```

Using and batched query and URL encoding the payload above, will solve the lab.

![[exploit.png]]

The response to the request takes around 10 seconds to come back, demonstrating that the payload works.

