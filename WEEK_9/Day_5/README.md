# Red Team 10: Privilege Escalation

## OUTLINE
- Overview
- General Techniques
- Kernel Exploits
- Service/Process Exploits
- Misconfigured Permissions
- Password Dumps

## PRIVILEGE ESCALATION
Privilege escalation is the act of exploiting a bug, design flaw or configuration oversign in an operating system or software application to gain elevated access to resources that are normally protected from an application or user.

- Start Recon Again!
- Don't forget about things you found during passive recon.
- Look for anything and everything you can find.
    - Pay attention to versions!
- Transfer helper tools over to your machine.
    - /usr/share/windows-resources
- Upgrade to a meterpreter shell!

<br>

## GENERAL TECHNIQUES
- Kernel Exploit
- Service/Process Exploits
- Password Cracking/Reuse
- Data Leaking
- Misconfigured Permissions
- Process Hijacking(Usually Windows only)

<br>

## KERNEL EXPLOITS
- Typically, a kernel exploit involves making a syscall with arguments designed specially to cause unintended behavior, despite the syscall attempting to only valid arguments.
- Often the inteded results of this exploit is spawning a root shell.
- It can also affect certain kernel defenses(modify permissions or /etc/shadow)

<br>

## SERVICE / PROCESS EXPLOITS
- Often takes advantage of a service that is running with higher permissions.
- This service can be running already or started as another user with a SUID bit.
- Trick the service into doing somethign it shouldn't!

<br>

## MISCONFIGURED PERMISSIONS
- Did you check which applications you can run without a password?
- Did you check what programs have an SUID bit set as root?

<br>

## PASSWORD DUMPS
- pwdump/fgdump
- Mimikatz
    - Pass The Hash
    - Priv Escalate
    - tons more modules: [Modules on Github](https://github.com/gentilkiwi/mimikatz/wiki)