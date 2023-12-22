#SQLiPAYLOAD 

# Recon

Test the stock check functionality and identify the `UNION` columns:


![[union-columns.png]]

In this case results are returned for only one column.

![[union-query.png]]

![[postgres-db.png]]

Now that we know the database provider and version enumerate the columns in the users table:

![[users-table-columns.png]]

Get usernames and passwords from the table

![[usernames.png]]

![[passwords.png]]

 Construct a query that retrieves the `administrator` password
![[SQLInjection/Attacks/1. Retrieving hidden data/labs/SQLi XML encoding bypass/images/admin-pass.png]]


Test the credentials with the administrator user