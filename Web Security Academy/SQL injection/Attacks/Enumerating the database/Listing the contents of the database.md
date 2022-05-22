# Listing the contents of the database
#DATABASEENUM 

Most databases except `Oracle` have a set of views called the information schema which provide information about the database.

## Listing database tables

Query `information_schema.tables` to list the tables of the database. As follows:

#SQLiPAYLOAD 
```SQL
SELECT * FROM information_schema.tables
```

That will return

![[tables.png]]

That indicates that there are three tables. Next enumerate the columns.

## Listing the database columns of each table

Query `information_schema.columns` to list the columns of each table of the database. As follows:

#SQLiPAYLOAD 
```SQL
SELECT * FROM information_schema.columns WHERE table_name = 'Users'
```

That will return

![[Attacks/Enumerating the database/images/columns.png]]

That indicates the columns on the specified table, in this case `Users`.

## Exploitation example

[[Non-Oracle databases listing contents]]