# Red Tean 01: Intro to Pentesting and Kali

## What is a pentest?
---
- `Penetration Testing`, also called pen testing or ethical hacking, is the practice of testing a computer system, network or web application to find security `vulnerabilities` that an attacker could `exploit`.
- Similar Terms - Ethical Hacking, Security Assessment, Red Teaming, White-hat hacking, Bug Bounties (Bug Bounty Programs)
    - All terms around identifying, proving, and then `reporting` security issues.
- Involves actual validation of these security weaknesses (i.e. actual demonstration of exploit via PoCs [proof of concepts]).
- Done from the `attacker's perspective`.

<br/>

## Four-Phase Pentest Process 
                    Information Gathering
                             ||
                             \/
                    Gaining Initial Access
                             ||
                             \/
                     Privilege Escalation
                             ||
                             \/
                      Post Exploitation

## Information Gathering
---
- Purpose: Learn sensitive information about the target useful for identify weaknesses and gaining a foothold on the system.
- Example Information:
    - `IP Addresses` (computers)
    - `Host Names` (purpose / type of device)
    - `Ports Open` (services)
    - `User Names` (employees)
    - `Services` (OS, specific version)

### Passive Information Gathering (OSINT)
---
- Bits `DO NOT` touch the target
- Purpose: Learn what is publicly available about the target
- Tools:
    - `theharvester` => usernames
    - `Google-dorking` => usernames, systems
    - `DNS tools` (sometimes) => hostnames, ips

### Active Information Gathering (Scanning)
---
- Bits `touch` the target
- Purpose: Learn more by directly interacting with your target
- Tools: 
    - `nmap` - targets (host discovery), ports (-p-), services (-sV), OS (-O), vulns (NSE --script, -A)
    - `OpenVAS` - vulnerabilities
    - Specific Protocol Scanners
        - WEB (`nikti`, `dirb`, `gobuster`, etc.)
        - SMB (`enum4linux`, `smbclient -L`)
        - FTP (`nmap`, `ftp`)

<br/>

## Gaining Initial Access
---
- Leverage some information gained (weakness) to get a foothold on the target
- Often time we'll want to leave ourselves an easier way to find our way back into the machines.
- Tools:
    - `metasploit`, `searchsploit`, `exploitdb`
    - `webshells`
    - `injextions`
    - `File inclusion`
    - And so much more....

<br/>

## Privilege Escalation
---
- Elevating your privileges to root / administrator (might need to be done multiple times)
- Give yourself a way back in
- Broad Categories:     
    - password reuse / password cracking
    - config files / script with creds
    - sudo / file permissions / groups
    - services with writeable executables
    - new ports / avenues of approach (i.e. internally accessible services)
    - Kernel exploits

<br/>

## Post Exploitation
---
- Recovering sensitive information from the target
- Things to look for:
    - Accounts and Cres (users, hashdump, /etc/shadow)
    - Who is using the system (network services, arp cache, logs)
    - User files (documents, pictires, etc.)
    - Service files (any databases, service code, admin scripts)
- Give yourself a way back in
- Clean up shop

# Summary:
- The four major parts of the pen-testing process include:
    1. Information Gathering
    2. Gaining Initial Access
    3. Privilege Escalation
    4. Post-Exploitation
- We often need to do a lot of information gathering at each spet of the way.
