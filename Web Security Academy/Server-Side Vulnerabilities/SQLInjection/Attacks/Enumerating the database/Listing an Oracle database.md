# Listing an Oracle database

The same information that can be obtained [[Listing the contents of the database]] of non-Oracle databases can be achieved with different queries.

## Listing all tables

List all tables by querying `all_tables`:

```SQL
SELECT * FROM all_tables
```

Read more about (column names to extract data) `all_tables` [here](https://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2105.htm#REFRN20286)

![[all_tables.png]]

## Listing columns of tables

Query the `all_tab_columns` table:

```SQL
SELECT * FROM all_tab_columns WHERE table_name = 'USERS'
```

Read more about (column names to extract data) `all_tab_columns` [here](https://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2094.htm)

![[all_tab_columns.png]]

## Exploitation example

[[Oracle database listing]]