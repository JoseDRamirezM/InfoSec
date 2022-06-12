# Database-specific factors

SQL language is mostly implemented in the same way across popular database platforms, many ways of detecting and exploiting SQL injections vulnerabilities work the same on different types of database. Though there are differences on some platforms and the way some techniques are performed changes in the following factors:

-   Syntax for string concatenation.
-   Comments.
-   Batched (or stacked) queries.
-   Platform-specific APIs.
-   Error messages.

Refer to [SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)for more detailed information on this.