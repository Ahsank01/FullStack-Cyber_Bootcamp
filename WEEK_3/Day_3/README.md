# Red Team 03: Active Information Gathering

## Active Reconnaissance
---
Active reconnaissance is a type of computer attack in which an intruder engages with the targeted system to gather information about vulnerabilities.

<br/>

## Agenda
---
- Understanding the Target
- `Nmap`
- Domain Name System `DNS` Enumeration
- Service Enumeration
- Web Enumeration

<br/>

## Understanding the Target
---
- Are you attacking a machine or a network?
- How many machines are on this network?
- Which machines should I target to find out information about the network?
- Which machines will give me the most access to the rest of the network?
- Which machines are the lowest hanginf fruit?
- Which machines will give me the most access to the rest of the network?
- Which machines are the lowest hanging fruit?

<br/>

## What is privileged access management
---
- It is a system used to safeguard an organization against the accidental or intentional misuse of privileged access
- A privileged user is someone who has administrative permissions to a critical company resource (database, file, etc.)

<br/>

## Understanding the Target
---
- Write a bash script to find out which machines are on the network.
- Write a bash script to find out which machines are running web servers on default `TCP` port 80

## NMAP - use cases
- Everything....
- Check which `machines` are `available` on a `network`
- Check which `ports` are `open` on a particular `machine`
- `Enumerate` the `services and versions` that are running on any particular `machine`
- Determine the `OS` and other `meta` `machine information`.
Run `scripts` that check if the machine is `vulnerable against particular attacks`.
And so much more!
- EX: `nmap` [ip address] -sV -A -0N results.txt

<br/>

## Active Reconnaissance - nmap highlighted options
    OPTIONS                           MEANING
      ||                                 ||
      \/                                 \/
    -p              Search a particular set of ports on targets. -p- for all ports.
    -O              Enable OS Detection
    -sV             Probe open ports to determine service/version info
    -Pn             Treat all hosts as if they are online
    -sU             Perform UDP Scan
    -A              Enable OS detection, version detection, script scanning and traceroute

<br/>

## Domain Name System (DNS) Enumeration
---
- Consider DNS servers to be your first thought when accessing a local network, this will help you map out the landscape.
- Getting a true network map is essentially like putting all of your targets on a silver platter
Many tools here: `host`, `dig`, `nslookup`, `dnseum`, `dnsrecon`, and more!
- EX: `nslookup` hackthissite.org
What we want: A `DNS` server willing to give us all of the information regarding available hosts on the network
- When do we want it: NOW!
- What we need: The domain name and DNS server

<br/>

## SMB Enumeration
---
- `Server Message Block` operates on `TCP` `139`, `445`
- This service allows communication between multiple machines and serves up information pertaining to password policies, usernames, group names, machine names, user and host SIDs and more
- `enum4linux` is a great tool for enumerating information from Windows and Samba systems
- EX: `enum4linux` -U -o [ip address]

<br/>

## Simple Mail Transfer Protocol (SMTP) Enumeration
---
- `SMTP` Servers are often used to send mail!
- `SMTP` supports several commands such as VRFY (verify) and EXPN (expand)
- Good tools include python scripts and smtp-user-enum
- EX: `smtp-user-enum` -u root -t [ip address]

<br/>

## Simple Network Management Protocol (SNMP)
---
- `UDP` based!
- Often overlooked in machines since we tend to focus on `TCP` services.

<br/>

## Web Enumeration
---
- In reality, our main point of entry is most likely to be over the web.
- We will commonly see web servers running on port `80`
- We can enumerate available paths/URLs on a website by using tools such as `dirbuster/gobuster` and `nikto`
- The idea is as follows:
    - `200` = I can go there!
    - `403` = Oh, so you don't want me to go there?
    - `500` = Why would this throw a server error?!
    - `400` = I don't care, not here

<br/>

## Web Enumeration - Tools
---
- `gobuster`
- `dirbuster`
- `Burp Suite`
- `curl`
- Eyes and Thoughts

<br/>

## Web Enumeration - gobuster/dirb
---
- `gobuster` dir -u URL -w WORDLIST (x32 - 2018-)
- `dirb` URL WORDLIST
- EX: `dirb` [ip address]/usr/share/wordlists/dirb/common.txt

<br/>

## Web Enumeration - nikto
---
- EX: `nikto` -h URL