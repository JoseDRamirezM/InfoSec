# 2FA bypass using a brute-force attack
#AUTHENTICATION 
#WRITEUP 

## Recon

Investigate the app given the credentials.

![[digits.png]]

A 2FA verification code is needed and it has 4 digits. 

If the code is entered incorrectly two times the user is redirected to the login page (logged out).

## Session handling

The nature of the application forces the attack to send a login request before any attempt on the 2FA code. Otherwise the requests will be rejected based on a CSRF token policy. For handling that (sessions) define a Macro in Burp Suite as follows:

Go to
- Project Options -> Sessions
	- Add a rule on Session Handling Rules
	- Include all URLs on the Scope tab
	![[session_rule.png]]

	- Go to the Details tab 
		- Add a rule
			- Run a macro
			- Record the macro with the necessary requests
			![[define_macro.png]]
		  - Test the macro and check the response to the last request, asking for input for the 4 digit code.
		  - Here I ran into a little problem, make sure in the `POST` request for `/login`, configure the csrf item to derive from the first response, otherwise the attack will not work.
		  ![[fix.png]]
  - Accept all changes and make sure to select the new rule in the Session Handling tab.

## Brute-forcing the code

Intercept the `POST` request to `/login2` and send it to the Intruder.

![[Vulnerabilities/labs/multi-factor authentication/2FA bypass using a brute-force attack/images/payload.png]]

Define the payload as usual, look into the `Resource Pool` tab and use a custom resource pool setting the Maximum concurrent requests to 1.

![[resource_pool.png]]

Start the attack.

