# Inducing conditional responses by triggering SQL errors

#BLINDSQLI 

Suppose the same scenario from [[Blind SQL injection with conditional responses]] but in this case the application does not behave any differently depending on whether the query returns any data. So Boolean conditions will no longer work as there's no difference to the application's response.

Though it's possible to induce conditional responses by triggering errors conditionally, depending on the injected condition. This is done by modifying the query so that it causes a database error if the condition is true, but not if the condition is false. Very often an unhandled error thrown by the database will cause some difference in the application's response (such as an error message) allowing to infer the truth of the injected condition.

## Using the CASE expression

Suppose two requests are sent injecting in the vulnerable cookie value.

```SQL
xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
```

The `CASE` expression evaluates in this case to `'a'`, when the condition of the `WHEN` expression is met, otherwise it evaluates to the `ELSE` expression. 

On the first case the `CASE` expression evaluates to `a`, as 1`!=`2. On the other hand the second expression evaluates to `1/0` as 1`=`1 triggering a `divide-by-zero` error. Assuming this causes some difference in the application's response, this can be used to infer whether the injected condition is true.

## Extract data

Similarly to [[Blind SQL injection with conditional responses]] extract data one character inferring the truth of the injected conditions.

```SQL
xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
```

	Different techniques will work best on different database types

## Exploitation example

[[Blind SQL injection with conditional errors]]





