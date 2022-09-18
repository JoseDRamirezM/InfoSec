# Authentication bypass via flawed state machine

#LOGICFLAWS 
#WRITEUP 
<hr>

## Recon

The lab says there's a way to bypass authentication, so first analyze the login process.

It follows these steps:
1. Provide credentials
2. Select role
3. Use the application with role restrictions

## Assessment

Flaws in the authentication flow may allow access to the `/admin` panel when skipping steps or altering the assumed flow.

## Exploitation

If the first step is completed and right after (skipping step 2) the `/admin` panel is requested, I got a 200 response and access to it. This may be caused because the role of the user is defined later in the flow, indicating the application is non-compliant with the principle of least privilege, giving each user administrator privileges while their role is defined.

![[BusinessLogic/labs/Authentication bypass via flawed state machine/images/bypass.png]]

![[admin_panel.png]]

Delete Carlos and the lab is complete.