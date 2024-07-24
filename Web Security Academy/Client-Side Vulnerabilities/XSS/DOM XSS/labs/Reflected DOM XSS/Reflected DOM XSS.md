This lab demonstrates a reflected DOM vulnerability. Reflected DOM vulnerabilities occur when the server-side application processes data from a request and echoes the data in the response. A script on the page then processes the reflected data in an unsafe way, ultimately writing it to a dangerous sink.

To solve this lab, create an injection that calls the `alert()` function.

The key to this lab is to READ the application script carefully:

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/Reflected DOM XSS/images/vuln.png]]

The script consumes an endpoint: 

`laburl/search-results?search=test`

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/Reflected DOM XSS/images/hint.png]]

And it returns an JSON object that is passed into a variable via the `eval` function (sink). Being able to manipulate the resulting JSON object will allow to execute arbitrary JavaScript code:

![[Client-Side Vulnerabilities/XSS/DOM XSS/labs/Reflected DOM XSS/images/query.png]]

The endpoint echoes the query param value:

![[AV.png]]

Manipulating the input will result in the JSON object and extra code as follows:

- Crafted result:
```json
{"results":[],"searchTerm":"test\\"};alert(1)//"}
```

- Script evaluation:
```javascript
eval('var x =' + {"results":[],"searchTerm":"test\\"};alert(1)//"})
```

Which results in XSS