# Examining the database
#UNION 
#DATABASEENUM 

Once a SQL injection vulnerability is found it's useful (imperative) to obtain information about the database. This information can be used to further exploitation.

Use a specific set of queries that depending on the database type, will return the version. For example in Oracle execute:

### Version

#SQLiPAYLOAD 
```SQL
SELECT * FROM v$version
```

It's also possible to enumerate the database tables and columns. The following query works on most databases to query the list of tables.

### Columns and tables
#SQLiPAYLOAD 
```SQL
SELECT * FROM information_schema.tables
```


[[Querying the database type and version]]

