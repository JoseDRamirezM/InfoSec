# Retrieving data from other tables writeup
#WRITEUP 
#UNION 

The SQL injection point is on the product category filter.

![[context.png]]

## Determine number of columns

![[SQLInjection/Attacks/UNION attacks/labs/SQL injection UNION attack, retrieving data from other tables/images/columns.png]]

## Determine which columns can hold string data

![[SQLInjection/Attacks/UNION attacks/labs/SQL injection UNION attack, retrieving data from other tables/images/string data.png]]

Both columns can hold string data.

## Craft the attack

The lab context says that there is a `users` table with the `username` and `password` columns.

So the payload is

```SQL
' UNION SELECT username,password FROM users--
```

Once placed in the injection point the following appears

![[SQLInjection/Attacks/UNION attacks/labs/SQL injection UNION attack, retrieving data from other tables/images/credentials.png]]

Next login as the `administrator` to solve the lab!

![[SQLInjection/Attacks/UNION attacks/labs/SQL injection UNION attack, retrieving data from other tables/images/solved.png]]