# Determining the number of columns required in an SQL injection UNION attack

#UNION

## Effective methods

### 1.  ORDER BY testing

Inject a series of `ORDER BY` clauses, incrementing the column index until and error occurs. 

#### Example

Assume the injection point is a quoted string within a `WHERE` clause of the original query, the payloads to inject are:

```SQL
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
' ORDER BY 4--
```
etc.

The `ORDER BY` clause modifies the original query to order the results by different columns in the result set. The columns on the result set can be referred by its index, so when the column index exceeds the number of actual columns in the result set, the database returns an error, such as

```SQL
The ORDER BY position number 3 is out of range of the number of items in the select list.
```

The way the application return the <font color="red">error</font> may vary. It can be in the HTTP response or in a generic error. If the attacker can detect a difference in the application's response, the number of columns of the result set can be inferred.

### 2.  UNION SELECT testing

The process is similar to the first method but the payload injected is `UNION SELECT`, this time increasing the number of null values as follows.

```SQL
' UNION SELECT NULL-- 
' UNION SELECT NULL,NULL-- 
' UNION SELECT NULL,NULL,NULL--
```

If the number of nulls does not match the number of columns, the database returns an error, such as

```SQL
All queries combined using a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists.
```

Identifying the error on the application's response may present as:
- Error message
- Generic error
- No result

When the number of `NULL` matches the number of columns, the database may return
- An additional row in the result set containing null values on each column
- An extra row on an HTML table
- Trigger a `NullPointerException` error

The amount of information and context that can be obtained from the response depends on the application's code. Worst case scenario the response does not have useful information for the attack.

# Oracle engine specifics

Using Oracle every `SELECT` query must use the `FROM` keyword and specify a valid table, there's a built-in table called `dual` which can be used for the attack, defining the payload as follows.

```SQL
' UNION SELECT NULL FROM DUAL--
```

Check the [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

# Exploitation

[[number of columns writeup]]
