# Pivoting target 1

Using the current Meterpreter session let's add a route to the unreachable network.

```
192.148.151.0/24
```

With the following command:

```bash
run autoroute -s 192.148.151.0 -n 255.255.255.0
```

![[autoroute.png]]

Then list that the route was created.

![[route_created.png]]

Now let's gather information on the network

[[Information gathering pivoted network]]