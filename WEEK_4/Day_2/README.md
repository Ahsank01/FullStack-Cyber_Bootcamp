# Red Team 07: Password Attacks
`P@ssword` is NOT a good `Password`

## OUTLINE
- Hashing Review
- Hash Types
- Password Attacking Scenarios
- Password Attack Methods
- Password Attack Tooling

<br>

## HASHING ALGORITHM
    Plain Test => Hash Function => Hashed Test (#b!c1d&uhfb3!@#4)

<br>

## HASHING
- Hash alogithms are one-way functions.
- Databases and other password storage mediums should hash their passwords.
- Good hash functions avoid collisions.
- Good hash functions have high entropy.
- Good hashing practices involce `salting`

<br>

## PASSWORD HASH CLASSES
- SHA
- NTLM
- LM
- MD
- Online classifier: [Hash Analyzer](https://www.tunnelsup.com/hash-analyzer/)

<br>

## PASSWORD ATTACK SCENARIOS
- Offline (Local)
    - We've gathered some passwords hashes and now we want to try to crack them.
- Online (Remote)
    - We are going to attempt to remotely try brute forcing a password.
    - Ex. Log-in form.
    - We need to consider defenses.

<br>

## PASSWORD ATTACKS METHODS
- Brute Forcing (Guessing)
    - Tries a password, compares to hash
    - Can be used against salted passwords
    - Works for local and remote
    - Small (computed at run time)
    - Can take a very long time
- Rainbow Table
    - List of pre-computed hashes linking password to hash
    - Potentially extremely large
    - Very quick with a big enough list
    - Can NOT be used against salted passwords
    - Notable mention: rainbowcrack tool in kali

<br>

## PASSWORD ATTACKS TOOLS
- Wordlists
    - Rockyou.txt
    - Cewl
    - Crunch
- Crackers
    - John
    - Hashcat
    - Hydra
    - Medussa
- Raindow Tables
    - [Crack Station](https://crackstation.net/)