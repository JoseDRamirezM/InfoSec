# Broken brute-force protection, multiple credentials per request

This lab was a little different as it used a different technology, it used JSON objects to transfer the data instead of the request body. Having this in mind try to put an array of strings instead of the single password string.

![[multiple.png]]

It didn't cause any errors on the application.

![[no_error.png]]

Hence generate a string with all the possible passwords and send the request.

![[worked.png]]

All passwords were evaluated, after that use the `Request in browser` option to obtain an URL where the user will be logged in.

![[repeat_browser.png]]

Go to the generated URL on the browser and the lab is solved.