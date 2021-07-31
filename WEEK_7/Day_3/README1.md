# Blue Team 08: Digital Forensics

## JOB OVERVIEW
- Potential Jobs:
    - Forensics Computer Examiner; Cyber Forensic Specialist; Forensic Consultants; etc.
- Typical Tasks:
    - Architect IT Systems so they are setup to collect evidence
    - Investigate and reconstruct an incident
    - Determine if data was exposed
    - Conduct audits

<br>

## OUTLINE
1. Digital Forensics
2. Forensic Toolkits (hardware / software)
3. Forensic Process
4. Targets

<br>

## DIGITAL FORENSICS
- `Forensics`: Scientific tests or techniques used in connection with investigating a crime
- `Digital Forensics`: Same thing, but with computers!
- Determine wha activities, changes, or other actions were performed on a system
- Who or what performed them
- What data is stored there

<br>

## DIGITAL FORENSICS: SYSTEMS
- Personal Computers
    - Desktops, laptops, smart watches
- Servers
    - Web servers. `dark` sites
- Phones/tablets (Even Kindles)
- Networks (pcaps!)
- Applications (esp, cloud)
    - Google Drive, email

<br>

## DIGITAL FORENSIC TOOLKITS
- Wide variety of hardware and software
    - Vary widely in cost and capability

<br>

## HARDWARE
- Workstation Requirements
    - Conducts data capture and analysis
    - Multicore CPU
    - Maximum ram 64GB+
    - Large and fast storage (SSD and large RAID array of images several TB)

<br>

## HARDWARE METAPHOR
- Think of your computer as a human body
    - The CPU(Central Processing Unit) is your brain:
        - It instructs your body what to do (and determines how many tasks and how fast it can do those tasks)
    - SSD (Solid State Drive) is your long term memory: 
        - Essential memories are stored here: How to eat, walk, talk, and scan network using nmap
    - RAM (Radnom Access Memory) is your short term memory:
        - This is like trying to remember what you wore to work on a Tuesday seven years ago.
    - We can already begin to see the concept of volatility start

<br>

## HARDWARE
- Write Blocker
    - Ensures that hard drives / SSDs cannot be written to retroactively
    - Hardware variants and software variants
- Faraday Cage
    - Used to block electromagnetic radiation
- Forensic Driver Duplicator
    - Designed to copy hard drives without changing original
    - Dedicated device that copies drive and hashed including slack and empty space
    - Free up forensic workstation
- Wipe drives and removable media
    - Clean drives that are ready to receive disk images
    - Prepared using drive wipe before use in the field
- Cables and drive adapters
    - Collection data in the field - especially if you work with LE
- Digital Camera
    - Photograpgh system layout, cabling, drivers, machine config.
- Documentation and Checklists
    - Chain of Custody Forms
    - Incident Response Forms and Processes

<br>

## SOFWARE
- Open source and commercial solutions for
    - Imaging - dd
    - Analysis
    - Hashing and validation - md5sum
    - Process and memory dumps - volatility
    - Password Cracking - hydra
    - Log viewing - Wireshark
    - Incident Response Forms and processes
- Imaging
    - Bit by bit copy of drive including slack space and unallocated
    - FTK and EnCase are commercial products
    - dd in linux, unix and mac
- Analysis
    - Create a timeline of system changes
    - Validate file against known good copy
    - File system analysis for hidden files, metadata, access
    - Windows registry analysis
    - Log parsing
    - FTK and EnCase are commercial products
- Process and Memory dumps
    - State of the OS and data in memory at time of collection
    - Hard to get without changing the contents
    - Hibernation files and crash dumps can also hold useful data

<br>

## DOCUMENTATIONS
- Chain of Custody forms, IR forms, plans and frameworks, etc.

<br>

# FORENSIC PROCESS
- What are the questions? Why investigate?
    - Knowing the goals will narrow down the `how`
- Outline the types of data and locations
- Document and review your plan
- Acquire and preserve evidence
- Perform initial analysis - document actions!
- Review your plan/analysis to guide deeper analysis
- Report on findings

<br>

## TARGETS: WHERE IS THE DATA?
- Forensic Artifacts
- What's being worked on right now?
    - Memory/RAM
- What is being talked about between multiple systems?
    - Networls
- What is and has been stored?
    - Hard disks, usb, etc

<br>

## TARGETS: VOLATILITY 
- Memory (RAM), cache, registers
- Network Traffic (pcaps)
- Disk Drives
- Optical disks, paper, cold storage

<br>

## SUMMARY
1. Digital Forensics is the investigation of a crime
2. You have been foloowing the forensic process already
3. Where to look to answer some forensic questions