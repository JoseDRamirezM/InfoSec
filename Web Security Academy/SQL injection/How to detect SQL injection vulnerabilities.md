# How to detect SQL injection vulnerabilities
#METHODOLOGY 

Manual systematic testing of:

- Submitting the single quote character `'` and looking for errors or anomalies.
- Submitting SQL-specific syntax that evaluates to the original value of an entry point and a to other values and looking for systematic differences.
- Submitting Boolean conditions such `1=1` and `1=2` and looking at the application's responses.
- Submitting payloads designed to trigger time delays and looking for differences in the time taken to respond.
- Submitting OAST payloads.

# SQL injection in different parts of the query

Most SQL injection vulnerabilities arise within the `WHERE` clause of a `SELECT` query. This type of SQL injection is generally well-understood by experienced testers.

But SQL injection vulnerabilities can in principle occur at any location within the query, and within different query types. The most common other locations where SQL injection arises are:

-   In `UPDATE` statements, within the updated values or the `WHERE` clause.
-   In `INSERT` statements, within the inserted values.
-   In `SELECT` statements, within the table or column name.
-   In `SELECT` statements, within the `ORDER BY` clause.

