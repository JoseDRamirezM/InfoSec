# Using an SQL injection UNION attack to retrieve interesting data
#UNION 

Once it's known
1. The number of columns of the result set
2. Which of those columns can hold string data

It's possible to return interesting data.

## Scenario

Suppose the following scenario

- The original query returns two columns, both of which can hold string data
-   The injection point is a quoted string within the `WHERE` clause.
-   The database contains a table called `users` with the columns `username` and `password`.

In this context retrieve the contents of the `users` table using the following payload

```SQL
' UNION SELECT username, password FROM users--
```

To perform the attack the `users` table name and the `username` and `password` columns are necessary. Otherwise the only options is guessing both table name and columns. All modern databases provide ways of examining the database structure, to determine tables and its columns.

