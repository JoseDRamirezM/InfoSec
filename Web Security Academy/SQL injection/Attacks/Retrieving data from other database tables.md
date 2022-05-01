# Retrieving data from other database tables

Consider the scenario of a user and password login, based on the user input the application performs an SQL query like so:

```
SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'
```

If the query returns the details of a user, hence a record exists for the user and the password is correct then the login is successful. Otherwise it fails.

In this case the attacker can log in as any user by simply appending the `--` comment indicator as follows:

```
SELECT * FROM users WHERE username = 'administrator'--' AND password = ''
```

The query returns the records for the `administrator` user and the login is successful.

