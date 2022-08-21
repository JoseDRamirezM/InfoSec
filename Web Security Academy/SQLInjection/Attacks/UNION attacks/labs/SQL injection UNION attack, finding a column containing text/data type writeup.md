# SQL injection UNION attack, finding a column containing text
#WRITEUP 
#UNION 

The same scenario from [[number of columns writeup]] is presented. 

The first step is to determine the number of columns of the result set.

![[scenario.png]]

The same number of columns is determined.

![[attack result.png]]

Then apply the following payloads on other `Intruder` attack:

```SQL
' UNION SELECT 'nAlKWn',NULL,NULL-- 
' UNION SELECT NULL,'nAlKWn',NULL-- 
' UNION SELECT NULL,NULL,'nAlKWn'--
```

![[data type payload.png]]

Placing the payload on the page the following appears:

![[reflection.png]]

The second column of the result set can hold string data. The lab is solved!