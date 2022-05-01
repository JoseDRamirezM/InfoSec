# SQL injection

![[SQLi_poster.png]]

SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It allows to retrieve data that is not normally available for the user. In some cases it may be possible to delete or modify the data causing persistent damage to the application.

Other possible threats are compromising the server/back-end infrastructure or to perform a [Denial of Service attack](https://www.paloaltonetworks.com/cyberpedia/what-is-a-denial-of-service-attack-dos)

# The impact of a successful SQL injection attack

1. Unauthorized access to sensitive data.
	- Causing reputational damage
	- Regulatory fines
2. In some cases obtaining a persistent backdoor into an organization's systems.

# SQLi examples
- Retrieve hidden data: return additional results modifying a SQL query.
- Subverting application logic: modify a query to interfere with the application logic.
- UNION attacks: retrieve information from different database tables.
- Examining the database: extract information about the version and structure of the database.
- Blind SQL injection: the results of a vulnerable query are not returned in the application response.
