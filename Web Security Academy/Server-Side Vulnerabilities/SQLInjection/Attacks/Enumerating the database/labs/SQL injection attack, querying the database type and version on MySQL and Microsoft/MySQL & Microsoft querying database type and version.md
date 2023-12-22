# MySQL & Microsoft querying database type and version

The lab mentions to use an UNION attack, following the [[Methodology UNION attacks]] attack the target.

## 1. Determine the number of columns of the result set

![[SQLInjection/Attacks/Enumerating the database/labs/SQL injection attack, querying the database type and version on MySQL and Microsoft/images/number of columns.png]]

The result set has two columns.

## 2. Determine which columns can hold string data

For some reason this step didn't work

![[number of columns 1.png]]

## 3. Exploitation

Retrieve the database version using the following payload.

#SQLiPAYLOAD 
```SQL
' UNION SELECT @@version,NULL--
```

![[SQLInjection/Attacks/Enumerating the database/labs/SQL injection attack, querying the database type and version on MySQL and Microsoft/images/solved.png]]