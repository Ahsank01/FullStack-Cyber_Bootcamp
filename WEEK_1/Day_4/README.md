# Essentials 04: OSI Model

### 7 Layers of the OSI Model
    - Application
        - End User Layer
        - HTTP, FTP, IRC, SSH, DNS
    - Presentation
        - Syntax Layer
        - SSL, SSH, IMAP, FTP, MPEG, JPEG
    - Session
        - Sync & send to port
        - API's Sockets, WinSock
    - Transport 
        - End-to-end connections
        - TCP, UDP
    - Network
        - Packets
        - IP, ICMP, IPSec, IGMP
    - Data Link
        - Frames
        - Ethernet, PPP, Switch, Bridge
    - Physical
        - Physical structure
        - Coax, Fiber, Wireless, Hubs, Repeaters

<br/>

## TCP vs. UDP
---
### TCP
- Reliable
- Connection-Oriented
- Segment retransmission
- Segment Sequencing
- Lots of overhead including 3-way handshake

### UDP
- Unreliable
- Not connection-oriented
- Packets lost and not retransmitted
- No packet numbering
- Very little overhead

<br/>

### TCP/IP
---
- We can use `nc` to check the tcp/ip protocols
- We can use `nc` to create a listener  
    - Open a port on our machine

<br/>

## nc
---
- A tool for arbitrary TCP and UDP connections.
- Can be used to set up listeners: `-l`
- Can be used to connect to listner (default)

<br/>

## Packet Sniffing
---
- We can use tools like `Wireshark` to listen to our network and observe traffic.

<br/>

## Packet Sniffing - Wireshark
---
- Chose your network
- Filter out noise:  
    - Set Capture Filters
    - Dynamically adjust Display Filters
- Create logs of capture (PCAP)