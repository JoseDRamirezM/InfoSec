# OAUTH 2.0 authentication vulnerabilities

Sites that let the user login with social media accounts. This functionality normally uses the OAuth 2.0 framework. It’s common to find implementation mistakes on this framework. This introduces vulnerabilities that may lead to obtain sensitive data and bypass authentication entirely.


## WHAT IS OAUTH
  
Is an authentication framework that allows applications to request limited access to an user account on other applications. This is done without exposing login credentials to a third party.


One example is when an application requests access to email contacts to suggest people to connect with. Also the users can log in with an account that is from a different website.

  

## HOW DOES OAUTH 2.0 WORK?

It defines the interaction of three parties

-   Client application: the website that requests the access to the user’s data.
    
-   Resource owner: The user with the information that the client wants to access
    
-   OAuth service provider: The website or application that controls the user’s data and access to it, this is done via an API so that the authorization server and the resource server can interact.
    

There are different ways in which the OAuth process can be implemented, these are known as  “flows” or “grant types”. This section will focus on **authorization code** and **implicit** grant types. Both types involve the following stages.

1. The client application requests access to a subset of the user's data, specifying the grant type and the kind of access.
2. The user logs in to the OAuth service and grants permission to the requested access.
3. The client application receives a access token to validate the authorization to get the user's data. This varies depending on the **grant type**.
4. The client application uses the access token to fetch information form the resource server via API calls.

Check [[OAuth grant types]] to understand more about the authentication process.

