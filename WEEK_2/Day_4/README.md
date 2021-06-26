# Essentials 09: Application Protocols

## Application Layer
---
### Outline
- OSI Model
- Application Layer
- Basic Tools
- Common Protocols

<br/>

## 7 Layers of the OSI Model
---
- `Application`  
    - End User Layer
    - HTTP, FTP, IRC, SSH, DNS
- `Presentation`  
    - Syntax Layer
    - SSL, SSH, IMAP, FTP, MPEG, JPEG

- `Session`  
    - Synch & send to port
    - API's, Sockets, WinSock
- `Transport`  
    - End-to-End Connections
    - TCP, UDP
- `Network`  
    - Packets
    - IP, ICMP, IPSec, IGMP
- `Data Link`  
    - Frames
    - Ethernet, PPP, Swtich, Bridge
- `Physical`   
    - Physical Structure
    - Coax, Fiber, Wireless, Hibs, Repeaters

<br/>

## Basic Tools: `netcat`
---
- `nc`
- The netcat utility is used for just about anything under the sun involving `TCP`, `UDP`, or other sockets!
```console
kali@kali:~$ nc <host> <port>
GET /HTTP/1.1
Host: <host>
User-AgentL netcat
```

## Basic Tools: `telnet`
---
- `telnet` = teletype network
- Plain text communications
- Default port 23
- Generally available on most systems!
```console
kali@kali:~$ telnet <host> <port>
```

<br/>

## Common Protocols
---
- `FTP` => Port 21
- `SMTP` => Port 25
- `SSH` => Port 22
- `HTTP` => Port 80
- `DNS` => Port 53

### FTP
    - File Transfer Protocol
    - Unencrypted
    - Port 21
    - Look for default logins or anonymous FTP
    - https://www.wired.com/2010/02/ftp_for_beginners/
### SMTP  
    - Simple Mail Transfer Protocol
    - Port 25
    - Look for enumerating users/valid email addresses
    - Send/receive mail!
    - https://computer.howstuffworks.com/e-mail-messaging/email3.htm
### SSH
    - Secure Shell
    - Port 22
    - Encrypted tunnel between machines!
    - Look for keys or access to authorized keys
    - https://www.hostinger.com/tutorials/ssh-tutorial-how-does-ssh-work
### Git
    - Version control system
    - Keeys history of files and commits
    - Set up SSH keys with GitHub
    - https://rogerdudler.github.io/git-guide/