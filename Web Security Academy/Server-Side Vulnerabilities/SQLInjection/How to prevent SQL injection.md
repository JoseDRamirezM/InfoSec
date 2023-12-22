# How to prevent SQL injection

- The problem

String concatenation of untrusted data into an SQL query.

- Recommendation

1. The use of `parametrized queries` also known as `prepared statements` when untrusted input appears as data within the query, next to the following keywords

- WHERE
- INSERT
- UPDATE
- ORDER BY

2. For a prepared statement to be effective on preventing SQL injection, the query string must be hard-coded and must never contain any variable data from any origin.

3. Never trust user data
4. Do not combine string concatenation with prepared statements in the applications queries even if the data is deemed to be `safe`, it only augments the probability of making a mistake and injecting an SQL injeciton vulnerability in the code.

## Examples

### Vulnerable code
```Java
String query = "SELECT * FROM products WHERE category = '"+ input + "'"; 
Statement statement = connection.createStatement(); 
ResultSet resultSet = statement.executeQuery(query);
```

### Protected code
```Java
PreparedStatement statement = connection.prepareStatement("SELECT * FROM products WHERE category = ?"); statement.setString(1, input); ResultSet resultSet = statement.executeQuery();
```

