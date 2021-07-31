# Blue Team 02: Recon & Vuln Scanning

## OULINE
1. Threat Categories
2. Threat Actors
3. Threat Modeling

<br>

## THREAT CATEGORIES (TOP LEVEL)
- `Known Threats` - Identifies with a signature or pattern matching (eg. Documented Exploits)
- `Unknown Threats` - Cannot be identified with signature or pattern matching (eg. Zero-day exploit, obfuscated malware, recycled threat, known unknowns, unknown unknowns)

<br>

## THREAT CATEGORIES
1. `Adversarial`
    - Deliberate undermining of organization's security
2. `Accidental`
    - Mistakes, especially during routine work
3. `Structural`
    - Something fails because of resource exhaustion, capacity, age, etc.
4. `Environmental`
    - Natural or man-made disasters

<br>

## THREAT ACTORS: CYBER
- Script-kiddie
- Hacking groups
- Hacktivists
- Black Hat professionals
- Organized criminal gangs
- Nation States

<br>

## MANY QUESTIONS TO ASK
1. How can an attack be performed?
2. What is the potential impact to a breach in the CIA of data?
3. How likely is the risk to occur?
4. What mitigations are in place?

<br>

## THREAT MODELS
- `Define your scenario` - What are your 'business' requirements?
- `Define your scenario` - What are your assests?
    - What do you care about?
    - What might attackers value?
- List out as many threats as you can!
    - How does each threat target an asset?
    - How does each threat attack CIA or AAA?
- Narrow your list of threats - what are you afraid of?
- Categorize and prioritize threats
- `Adversary Capability` - Formal classification of the resources and expertise of a threa actor
- `Attack Surface` - The points at which a network or application receives external connections or inputs/outputs that are potential vectors to be exploited by a threat actor
- `Attack Vector` - Specific path by which a threat actor gains unauthorized access to a system

<br>

## THREAT MODELS: OTHER WAYS
1. Vulnerability-first
    - Enumerate vulnerabilities, possibly with scanners
    - Create a threat model based on relevant threats
2. Tool-based
    - Microsoft Threat Modeling Tool
    - Create data flow diagram, tool suggests common threats

<br>

## SUMMARY
- We use categories to label threats
- Categorizing threats will help with assessing severity and likelihood
- Threat models help define what is "in scope"
- You will defend against what is in the threat model.