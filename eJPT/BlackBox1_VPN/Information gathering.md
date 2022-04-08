# Information gathering

## First steps

From INE's PTS lab here's the objective.

- You have been engaged in a Black-box Penetration Test (**172.16.64.0/24** **range**). Your goal is to read the flag file on each machine. On some of them, you will be required to exploit a remote code execution vulnerability in order to read the flag.

Next I connected to the lab VPN environment.

Once connected I got access to the mentioned network segment.

![[scope_network.png]]

## Host discovery

I ran performed host discovery with nmap:

`sudo nmap -sn -n 172.16.64.0/24`

![[network_hosts.png]]

I found 4 up host (not counting my machine).

I gave each host a nickname


| Host        | Nickname    |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

Now scan the hosts.

[[Footprinting and scanning]]