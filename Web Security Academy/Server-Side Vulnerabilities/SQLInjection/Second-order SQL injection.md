# Second-order SQL injection

`First order` SQL injection occurs when the application takes user input from an HTTP request and when processing it incorporates the input into an SQL query in an unsafe way.

`Second order` SQL injection (also known as Stored SQL injection),  refers to when the application takes user input from an HTTP request and stores it for future use. This is usually done by placing the input into a database. The vulnerability doesn't arise when storing data, but when the application retrieves the stored data and incorporates it into an SQL query in an unsafe way.

![[2nd_order.png]]

`Second order` SQL injection often arises where developers are aware of SQL injection vulnerabilities, the input placement into the database is handled safely. Then when the data is retrieved it is handled insecurely as it is deemed to be `safe`.
