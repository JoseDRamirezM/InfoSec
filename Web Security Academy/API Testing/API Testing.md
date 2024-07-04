APIs enable software systems and applications to communicate and share data. Vulnerabilities in APIs may undermine core aspects of a website's confidentiality, integrity and availability. All dynamic websites are composed of APIs, testing classic server-side vulnerabilities also apply here. Knowing how to test fully used by the website front-end focusing on RESTful and JSON APIs.

# API Recon

Before testing try to find out as much information about the API as possible, to discover its attack surface.

1. Identify API endpoints

These are locations where the API receives requests about a specific resource on its server. Its important to determine the endpoints and how to interact with them, allowing to construct HTTP requests for the API, doing this will allow:

- Know the API processes, including mandatory and optional parameters
- Types of requests the API accepts, supported HTTP methods and media formats
- Rate limits and authentication mechanisms

# API Documentation

APIs are usually documented for developers know how to use and integrate with them. This documents can be either human or machine readable, including detailed explanations, examples and usage scenarios. Machine-readable documentation may have to be parsed from JSON or XML and its often used for integration an validation purposes.

Often times API documentation is publicly available, particularly if the API is intended for use by external developers.

## Discovering API documentation

Even if the documentation is not public, its worth a try to browse the API on common routes.

- `/api`
- `/swagger/index.html`
- `/openapi.json`

Always investigate base paths e.g `/api/swagger/v1/users/123` to investigate:

- `/api/swagger/v1`
- `/api/swagger`
- `/api`

Listing common paths to find documentation using Intruder is also an option.

[[1. API Documentation]]

## Using machine-readable documentation

Many tools can be used to parse this information when found.


- Burp scanner
	- OpenAPI
	- JSON
	- YAML
- OpenAPI parser
- Postman
- SOAPUI

## Identifying API endpoints

Another approach is to browse or interact with the application that uses the API. Doing this is always good even if the attacker has access to documentation as it can be inaccurate or out of date. 

Burp Scanner can be used to crawl the application and manually investigate interesting attack surface.

Look for:

- Endpoints that suggest the use of an API such as:
	- `/api/`
- JavaScript files may contain references to API endpoints that are not triggered directly via the web browser.
- [JS Link Finder](https://portswigger.net/bappstore/0e61c786db0c4ac787a08c4516d52ccf) for a deeper search

### Interacting with API endpoints

Once API endpoints are identified, observe the API's behavior to discover additional attack surface.

Tests:

- Change the HTTP method and media type
	- Review possible error messages
		- These can be useful to construct a valid HTTP request
	- See how the API behaves

#### Identifying supported HTTP methods

The HTTP method specifies the action to be performed on a resource. For example:

- `GET` - Retrieves data from a resource.
- `PATCH` - Applies partial changes to a resource.
- `OPTIONS` - Retrieves information on the types of request methods that can be used on a resource.

An API endpoint may support different HTTP methods. It's therefore important to test all potential methods when you're investigating API endpoints. This may enable you to identify additional endpoint functionality, opening up more attack surface.

For example, the endpoint `/api/tasks` may support the following methods:

- `GET /api/tasks` - Retrieves a list of tasks.
- `POST /api/tasks` - Creates a new task.
- `DELETE /api/tasks/1` - Deletes a task.

You can use the built-in **HTTP verbs** list in Burp Intruder to automatically cycle through a range of methods.

	Note
	
	When testing different HTTP methods, target low-priority objects. This helps make sure that you avoid unintended consequences, for example altering critical items or creating excessive records.
	
#### Identifying supported content types

API endpoints often expect data in a specific format. They may therefore behave differently depending on the content type of the data provided in a request. Changing the content type may enable you to:

- Trigger errors that disclose useful information.
- Bypass flawed defenses.
- Take advantage of differences in processing logic. For example, an API may be secure when handling JSON data but susceptible to injection attacks when dealing with XML.

To change the content type, modify the `Content-Type` header, then reformat the request body accordingly. You can use the [Content type converter](https://portswigger.net/bappstore/db57ecbe2cb7446292a94aa6181c9278) BApp to automatically convert data submitted within requests between XML and JSON.

Useful tool

[Content Type Converter](https://portswigger.net/bappstore/db57ecbe2cb7446292a94aa6181c9278)

#### Using Intruder to find hidden endpoints

Once you have identified some initial API endpoints, you can use Intruder to uncover hidden endpoints. For example, consider a scenario where you have identified the following API endpoint for updating user information:

`PUT /api/user/update`

To identify hidden endpoints, you could use Burp Intruder to find other resources with the same structure. For example, you could add a payload to the `/update` position of the path with a list of other common functions, such as `delete` and `add`.

When looking for hidden endpoints, use wordlists based on common API naming conventions and industry terms. Make sure you also include terms that are relevant to the application, based on your initial recon.

## Finding hidden parameters

When you're doing API recon, you may find undocumented parameters that the API supports. You can attempt to use these to change the application's behavior. Burp includes numerous tools that can help you identify hidden parameters:

- Burp Intruder enables you to automatically discover hidden parameters, using a wordlist of common parameter names to replace existing parameters or add new parameters. Make sure you also include names that are relevant to the application, based on your initial recon.
- The [Param miner](https://portswigger.net/bappstore/17d2949a985c4b7ca092728dba871943) BApp enables you to automatically guess up to 65,536 param names per request. Param miner automatically guesses names that are relevant to the application, based on information taken from the scope.
- The [Content discovery](https://portswigger.net/burp/documentation/desktop/tools/engagement-tools/content-discovery) tool enables you to discover content that isn't linked from visible content that you can browse to, including parameters.

### Mass assignment vulnerabilities

Mass assignment (also known as auto-binding) can inadvertently create hidden parameters. It occurs when software frameworks automatically bind request parameters to fields on an internal object. Mass assignment may therefore result in the application supporting parameters that were never intended to be processed by the developer.

#### Identifying hidden parameters

Since mass assignment creates parameters from object fields, you can often identify these hidden parameters by manually examining objects returned by the API.

For example, consider a `PATCH /api/users/` request, which enables users to update their username and email, and includes the following JSON:

```
{ "username": "wiener", "email": "wiener@example.com", }
```

A concurrent `GET /api/users/123` request returns the following JSON:

```
{ "id": 123, "name": "John Doe", "email": "john@example.com", "isAdmin": "false" }
```

This may indicate that the hidden `id` and `isAdmin` parameters are bound to the internal user object, alongside the updated username and email parameters.

#### Testing mass assignment vulnerabilities

To test whether you can modify the enumerated `isAdmin` parameter value, add it to the `PATCH` request:

```
{ "username": "wiener", "email": "wiener@example.com", "isAdmin": false, }
```

In addition, send a `PATCH` request with an invalid `isAdmin` parameter value:


```
{ "username": "wiener", "email": "wiener@example.com", "isAdmin": "foo", }
```

If the application behaves differently, this may suggest that the invalid value impacts the query logic, but the valid value doesn't. This may indicate that the parameter can be successfully updated by the user.

You can then send a `PATCH` request with the `isAdmin` parameter value set to `true`, to try and exploit the vulnerability:

```
{ "username": "wiener", "email": "wiener@example.com", "isAdmin": true, }
```

If the `isAdmin` value in the request is bound to the user object without adequate validation and sanitization, the user `wiener` may be incorrectly granted admin privileges. To determine whether this is the case, browse the application as `wiener` to see whether you can access admin functionality.

## Preventing vulnerabilities in APIs

When designing APIs, make sure that security is a consideration from the beginning. In particular, make sure that you:

- Secure your documentation if you don't intend your API to be publicly accessible.
- Ensure your documentation is kept up to date so that legitimate testers have full visibility of the API's attack surface.
- Apply an allowlist of permitted HTTP methods.
- Validate that the content type is expected for each request or response.
- Use generic error messages to avoid giving away information that may be useful for an attacker.
- Use protective measures on all versions of your API, not just the current production version.

To prevent mass assignment vulnerabilities, allowlist the properties that can be updated by the user, and blocklist sensitive properties that shouldn't be updated by the user.