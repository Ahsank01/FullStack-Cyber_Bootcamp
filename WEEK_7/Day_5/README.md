# Essentials 10: Windows Command Prompt

## Outline:
- cmd.exe
- Navigation
- Creating/Modification/Deletiom
- Searching
- I/O Redirection
- Management
- Summary

<br/>

## cmd.exe
---
- Start > Command Prompt
- Case insensitive
- Run as `administrator` - elevates `privileges`
- `help [command]`
- `(command)/?`
- Options use `/` instead of `-`
- Right click on the menu bar to get copy/other options
- `cls`

## Navigation
---
- Drives - `Z:`, `C:`
- Similar to Linux with folder structure and working directory
- Commands:  
    - `cd`
    - `dir`

## Navigation - Where am I?
- Where am I? - `change directory`
- `cd`

## Navigation - List all the directories!
- `dir`
- Try `/a` for hidden files

## Navigation - Take me there!
- "change directory"
- `cd (directory)`
- Uses `\`
- Drives are different
- `Z:`

## Navigation - Take me back?
- Same as Linux
- `.` => current directory
- `..` => parent directory

## Create / Modification / Deletion
- New File  
    - type nul > file.txt
    - echo foo > file.txt
- File contents
    - type file.txt
- Move/Copy  
    - move (source) (dest)
    - copt (source) (dest)
- Delete  
    - del file.txt
    - rmdir (directory)

## Searching - File contents
- `find` kind of like `grep`
- Must use quotes for search term

## I/O redirection
- `<` to get content from a file
- `>` to overwrite a file
- `>>` to append to a file

## Management
    - `net [option]`
    - Let's you manage a ton of different settings