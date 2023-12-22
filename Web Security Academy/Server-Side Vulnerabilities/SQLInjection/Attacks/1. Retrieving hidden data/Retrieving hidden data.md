# Retrieving hidden data

Consider the following scenario.

A shopping application that displays products in different categories, making a request to the URL:

```
https://insecure-website.com/products?category=Gifts
```

The application executes an SQL query to retrieve the details of products from the database.

```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

In this scenario if the application doesn't implement defenses against SQL injection attacks all products can be retrieved from the database using an always true statement.

### Always true statement and comment indicator on SQL

The attack string is `OR 1=1 --`  , where `OR 1=1` is an always true statement that will retrieve all items. 
If the attacker can inject the statement and the `--` characters make the rest of the query to be an SQL comment. Thus controlling the query and making it possible to retrieve hidden data from the database.

### Injection on URL

```
https://insecure-website.com/products?category=Gifts'+OR+1=1--
```

### Resulting query to the database

```
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
```

# SQL Injection in different contexts

Injections can happen in any controllable input that is processed as a SQL query by the application. Some applications may take JSON or XML format to use it on the database.

These formats can provide ways to obfuscate attacks that are otherwise blocked by WAFs and other defense mechanisms. Weak filter implementations often look for common SQL injection keywords within the request so these controls may be bypassed by encoding or escaping characters.

## Payload using XML escape sequence

XML escape sequence to encode the `S` character in `SELECT`:

```XML
<stockCheck>
	<productId>
		123
	</productId>
	<storeId>999 &#x53;ELECT * FROM information_schema.tables</storeId> 
</stockCheck>
```
This will be decoded server-side before being passed to the SQL interpreter.


