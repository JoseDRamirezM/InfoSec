# Retrieving data from other tables writeup
#WRITEUP 
#UNION 

The SQL injection point is on the product category filter.

![[context.png]]

## Determine number of columns

![[Attacks/UNION attacks/labs/SQL injection UNION attack, retrieving data from other tables/images/columns.png]]

## Determine which columns can hold string data

![[Attacks/UNION attacks/labs/SQL injection UNION attack, retrieving data from other tables/images/string data.png]]

Both columns can hold string data.

## Craft the attack

The lab context says that there is a `users` table with the `username` and `password` columns.

So the payload is

```SQL
' UNION SELECT username,password FROM users--
```

Once placed in the injection point the following appears

![[credentials.png]]

Next login as the `administrator` to solve the lab!

![[Attacks/UNION attacks/labs/SQL injection UNION attack, retrieving data from other tables/images/solved.png]]