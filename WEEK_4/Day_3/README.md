# Red Team 08: Metasploit

## METASPLOIT
Metasploit is a penetration testing framework that makes hacking simpler
- It is a comprehensice hacking framework consisting of `thousands` of modules.
    - To launch the console run: `msfconsole`
- Metasploit require postgresql to cache exploits and improve performance.
    - To start postgres: `service postgresql start`
    - To cache in the consolde: `db_rebuild_cache`

<br>

## METASPLOIT - COMPOSITION
- Exploits
- Auxiliary
- Post
- Additional Tools

    ### EXPLOITS
    - Find exploits in metasploit use the search functionality
    - Unfortunately, these results can be wildly different than searchsploits reults.
    - Enter `supersploit!`

    ### Auxiliary
    - Set of tasks that are generally not used to compromise systems.
    - Can be used to verify, check, soft/hard test, scope out, and more.
    - There are over 1000 auxiliary modules.

    ### POST
    - Generally used post exploitation
    - Can assist in recon or escalation

<br>

## METASPLOIT COMMAND FORMAT
COMMADS => Meaning  
use => Load a module into metasploit  
exploit => Launch a module  
show => Show some particular things within metasploit (payloads, options, etc.)  
set => Set a value of an option within metasploit  
sessions => Bring up a list of current sessions within metasploit