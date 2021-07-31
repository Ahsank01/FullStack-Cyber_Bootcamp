# Blue Team 03: Firewalls & IDS

## OUTLINE
1. Protect
2. Preventing Recon
3. Firewalls

<br>

## PROTECT
- How do you protect your systems, people, data?
- How do you stop passive/active recon?
- How do you configure logging systems?
- What tools or techniques can you leverage?
- Where do you prioritize effort?

<br>

## PREVENTING RECON
- Limit services/attack surface
    - Block Ping
- IDS/IPS
    - snort, bro
- Harden DNS servers
    - Don't allow zone transfers to just anyone!
- Whois privacy services
- Social media policies

<br>

## FIREWALLS
- A device or software designed to filter network traffic
    - Allow, Block, (other)
- Packet filtering
- Stateful inspection
- Application-specific firewalls
- Next generation

<br>

## FIREWALLS: OSI LAYERS
- Packet filtering
- Stateful inspection
- App firewalls
- Next generation

<br>

## FIREWALLS: PLACEMENT
- On your host
    - Between your applications and the network
- At network segment boundaries
    - Between one network segment (LAN) and another (DMZ)
- On your home router
    - Between your local network (LAN) and the internet (WAN)

<br>

## FIREWALLS: HOST-BASED
- Windows 
    - Defender
    - Group Policy
- MAC
    - Security Preferences
    - Lulu
- Linux
    - Iptables
    - UFW

<br>

## SUMMARY
1. Firewalls filter, block, and analyze network traffic
2. Types of firewalls
    1. Packet filtering
    2. Stateful inspection
    3. App firewalls
    4. Next generation