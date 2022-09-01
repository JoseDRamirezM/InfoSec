# Excessive trust in client-side controls

Fundamentally flawed assumptions regarding this are:

- The user will only interact with the application via the provided web interface. 
- Client-side validation will prevent users from supplying malicious input. (using a proxy will bypass all client-side controls)
- Trusting user input i.e not performing
	- Integrity checks
	- Server-side validation

## Exploitation examples

- [[Lab Excessive trust in client-side controls]]
- [[2FA broken logic]]
