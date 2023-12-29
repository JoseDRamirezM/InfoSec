# UNION attacks columns lab write up
#WRITEUP 
#UNION 

The injection point is in the product filter.

![[filters.png]]

Once a filter category is clicked the following request is made

![[Server-Side Vulnerabilities/SQLInjection/Attacks/UNION attacks/labs/SQL injection UNION attack, determining the number of columns returned by the query/images/request.png]]

Then I confirmed the SQL injection vulnerability.

![[sqli confirmed.png]]

Then as the lab description says, determine the number of columns by injecting `UNION SELECT` clauses. 

## Exploitation

I intercepted the request and sent it to `Burp's Intruder` and placed the following payloads

![[SQLInjection/Attacks/UNION attacks/labs/SQL injection UNION attack, determining the number of columns returned by the query/images/intruder.png]]

![[payloads.png]]

Then I started the attack.

![[attack result.png]]

It was easy to say that the number of columns on the result set is 3. And the lab was solved.