# Red Team 04: Shells and Shellcode

## Outline
- Overview
- Shells
- Payloads
- Tooling

<br/>

## Shells
In computing, a shell is a user interface for access to an operating system's services.

<br/>

## Types of Shells
- `Bash`
- `Zsh`
- `Sh`
- `Web Shells`

<br/>

## Payloads
When exploiting an application, the payload is the code that the attacker actually wants to execute and often contains shell code.

<br/>

## Categories of Shell Payloads
- `BIND` - The shell to be shared is bound by the `listner`.
    - In most cases: we are reponsible for connecting to it.
- `REVERSE` - The shell to be shared is bound by the `connector`.
    - In most cases: we are responsible for opening a port and listening for an incoming connection

<br/>

## Payloads with `nc`
- Use the `-e` option!

<br/>

## Payload Generation
- Target Operating System
- Target Architecture
- Type of payload
- Type of Shell
- Destination of File Execution
- Connection Type

<br/>

## Target Operating System
- Windows
- Linux
- MacOSX
- Unix
- Android
- iOS

<br/>

## Target Architecture
- `x86`
- `x64`

<br/>

## Types of Shells
- Command Prompt
- Bash Shell
- #Meterpreter*

<br/>

## Root
- Windows Executable
- Linux Elf
- Bash
- Web Service / Other Network Service

<br/>

## Type of Payload
- `Unstaged Payloads`
    - The entire payload is sent at one time
    - Can be caught by nc or netasploit
    - Generate a ton of traffic
    - Fairly easy to detect by firewall or Antivirus (AV)
- `Staged Payloads`
    - These payloads are initially incomplete
    - Require a mechanism to distribute remainder of payload over time.
    - Good for avoiding AV and firewall detection
    - Must be caught by metasploit

<br/>

## msfvenom
    OPTIONS                            MEANING
      ||                                  ||
      \/                                  \/
    -p                      Set a payload -p linux/x64/shell_reverse_tcp
    -f                      Output format/file type elf, exe, py, c, etc.
    LPORT=                  IP address of port to connect back to on connecting machine or IP address of port to open on host machine (bind shells)
    LHOST=                  IP address of machine to connect back to (usually attacker's ip address)
    --list                  List options in a particular category --list payloads

<br/>

## Transferring Files with Netcat
To transfer file from kali to windows system, we will set up a netcat listner on port 4444 and redirect any output into a file called `incoming.exe`
```console
C:\Users\offsec> nc -nlvp 4444 > incoming.exe
listening on [any] 4444
```
On kali, we will push the wget.exe file to the windows machine through TCP port 4444:
```console
kali@kali:~$ nv -nv 10.11.0.22 4444 < /usr/share/file.exe>

python -c 'import pty; pty.spawn("/bin/bash")'
