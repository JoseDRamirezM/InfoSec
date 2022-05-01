# LAB Improper implementation of the implicit grant type

This lab starts by presenting an interface where there's a `My account` button

![[interface_account.png]]

Once clicked it starts an OAuth flow for the implicit grant type and after it completed the user `wiener` was logged in.

Intercepting the requests I noticed that there was a script that logged the user in using the `/authenticate` endpoint.

![[save_user_sess_script.png]]

It submitted the user's <font color=yellow>email</font>, <font color=yellow>username</font> and the <font color=yellow>access token</font> in a `POST` request.

![[save_sess_req.png]]

Then as the objective of the lab is to impersonate the user with the email `carlos@carlos-montoya.net` I changed the user email and forwarded the request.

![[impersonate.png]]

After that checking the `My account` page I could see that I was logged in as the objective user and the lab was solved.

![[lab_solved.png]]



