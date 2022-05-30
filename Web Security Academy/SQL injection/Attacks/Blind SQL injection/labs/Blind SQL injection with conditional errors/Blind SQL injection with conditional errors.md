# Blind SQL injection with conditional errors
#BLINDSQLI #WRITEUP 

For this lab the payload is hard to construct as the database technology can't be enumerated easily, but rather has to be guessed (or read the lab hint).

Start by trying a simple payload evaluating a condition using the `CASE` statement as follows:

```SQL
'+AND+(SELECT+CASE+WHEN+(1=2)+THEN+to_char(1/0)+ELSE+'a'+END from dual)='a
```

This causes no error, but when the condition is `1=1` a 500 error is generated on the page.

Generating the scenario showed on the theory [[Inducing conditional responses by triggering SQL errors]]. Hence now it's possible to get character by character the administrator password, I will use the script that I wrote on [[Blind SQL injection with conditional responses]] but adapting it to the scenario.



