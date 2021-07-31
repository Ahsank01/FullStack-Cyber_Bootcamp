# Blue Team 02: Recon & Assest Management

## OUTLINE
1. Identify / Enumeration
2. Asset Management
3. Active Recon
4. Passive Recon

<br>

## ENUMERATION REVIEW
- `Enumeration`
    - Process to identify and scan network ranges and hosts of a target and mapping an attack surface
- `Active`
    - A connection is made and data is transmitted between attacker and target
- `Passive`
    - No connection is made between attacker an target
- What vulneravilities do your systems have?
- What are your risks?
- Who needs to know these answers?
- Who do you need to inform? Why?

<br>

## IDENTIFY
- What/who are protecting?
- Why are you protecting that?
- What threats are you afraid of?
- What vulnerabilities do your systems have?
- What are your risks?
- Who needs to know these answers?
- Who do you need to inform? Why?
- People
- Asset inventory
- Network maps
- Dependencies
- Vulnerabilities
- Threats
- Risks

<br>

## ASSET MANAGEMENT
- Track assets and associate identifies from all sources
- Lots of different solutions and vendors
- Given some information (hostname, IP Address, etc.) can we find all associated devices?
- Time is a key aspect for many fields
    - Computer may be viped and re-used
    - DHCP leases may change on renewal

<br>

## ASSET MANAGEMENT: IDENTIFIERS
- Asset unique ID - we create this!
- Device/hardware info - asset tags
- People and authorized users
    - Who was this device issued to? Connect to organizational chart?
- Physical location
    - Which department or office was this device issued to?
- Operating system and installed software
    - What is running on this machine?
    - What software licenses are active?
- Network Identifiers!
- MAC Address
- IP Address
- Hostname
- Certificates (user and device)
- Autheticated Users
- Backup or patch status
- Security log status

<br>

## ASSET MANAGEMENT
- Time is a key aspect for many fields
- Record changes with timestamps
- Link identifiers across different layers and different sources

<br>

## AVTIVE RECON
- Activity that can be seen or logged
- Port Scanners!
    - Nmap, Angry IP, other tools
- External vs Internal
- Vulnerability Scanners

<br>

## PASSIVE RECON
- Packet Analysis
    - Netflow
- Log Analysis
    - Routers, switches, DHCP, DNS, Firewalls
- Configuration Files
    - Network Devices
- Host configurations
    - Applicatiosn (installed/running)
- Domains, IP blocks, certificates
- Organization data

<br>

## SUMMARY
1. Identify what and who you are protecting. Know why and against what threats.
2. Asset management is critical for cybersecurity
3. Passive recon gets new tricks