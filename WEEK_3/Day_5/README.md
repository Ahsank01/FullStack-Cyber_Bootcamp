# Red Team 05: File Trasnfers

## FTP Practice
---
1. Install and start up pure-ftpd in your Kali Machine if you haven't already.
2. Generate a reverse shell payload that will appropriately target your windows 10 client lab machine and place it in your /ftphome folder.
3. Attempt to transfer this shell to your windows machine using the ftp-user you created when installing pure-ftpd. Execute the payload to ensure it works (don't forget to catch/connect)!
4. File corrupted? Check out these [common FTP commands](https://www.exavault.com/blog/app/uploads/2018/10/20_ftp_commands.pdf). Maybe one will be helpful?
5. Use only `echo` in your windows command prompt [follow these steps](https://sushant747.gitbooks.io/total-oscp-guide/transfering_files_to_windows.html) to transfer that payload to your windows machine in non-interactive mode.
6. Transfer a file to your Windows machine `without` using the interactive FTP shell. Instead create a script on the command line to transfer the file.

<br>

## HTTP Practice
---
1. Generate a reverse php shell using `msfvenom`.
2. Transfer that shell to your Debian Client using HTTP. Will Apache work for serving the file? What will you use to download the file?
3. Start a listener on your machine, and then execute the php shell. How do you execute a web shell?

<br>

## Certutil
---
1. Use the `certutil` utility to transfer a file to your Windows machine.
2. [Official documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certutil)
