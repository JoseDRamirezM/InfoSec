# UNION attacks
#UNION 

If the application is vulnerable to SQL injection and the results of the query are reflected on the application's responses, the `UNION` keyword allows to retrieve data from other tables on the database. This is known as an SQL injection UNION attack.

The `UNION` keyword is used to execute additional `SELECT` queries and append the results to the original query.

## Example

```SQL
SELECT a, b FROM table1 UNION SELECT c, d from table2
```

This SQL query will return a single result with two columns, containing the values of `a`, `b` in `table1` and `c`, `d` in `table2`.

## Conditions

The following conditions must be met to an `UNION` attack to be possible.

- All the queries must return the same number of columns.
- The data types returned in each query must be compatible.

## Information needed

To perform the attack the following information is necessary

- How many columns are being returned from the original query?
- Which columns returned from the original query are of a suitable data type to hold the results from the injected query?