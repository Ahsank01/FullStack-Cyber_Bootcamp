# Blue Team 01: Fundamentals & Threat Models

## OUTLINE
1. Penetration Testing
2. Cybersecurity Jobs
3. Why did we teach offense first?
4. Blue Team Overview
5. CySA+
6. Fundamentals

<br>

## PENETRATION TESTING
- Planning > Discovery > Attack > Reporting
- `Attack` = (Recon), Exploitation, Privilege Escalation, Post-Exploit
- `Planning` = Getting Permission!
    - Timing, Scope, and Authorization
- `Discovery` = Recon, but may also include extra information from the Blue Team
- `Reporting` = You have to tell people what you found!

<br>

## CYBERSECURIY JOBS
1. Peneration Testing
2. Security Assessments
3. Security Analyst/Engineer
4. Incident Management
5. Digital Forensics
6. Threat Analysis
7. Cyber Security Policy
8. ... and so many more

<br>

## 'ANALYST' FUNCTIONS
- Implement and configure security controls
- Working in a SOC or CSIRT
- Auditing security processes amd procedures
- Conducting risk assessments, vulnerability assessments, and penetration test
- Maintaining up-to-date threat intelligence
- Legal, compliance, and regulatory issues
- ... and so many more

<br>

## SOCs
1. A location where security professionals monitor and protect critical information assests in an organization.
2. Usually exist for larget orgs (eg. Government, large corporations, health care orgs.)
3. Have the authority to operate (SOC is empowered)
4. Contain motivated, skilled, skeptical professionals
5. Perform incident response
6. Protect itself and the org.
7. Separate 'signal from noise'
8. Collaborate with other SOCs

<br>

## IS THIS OFFENSE OR DEFENSE?
- Command line tools (grep, find, netstat, chmod)
- Network captures (cpdump, wireshark, pcaps)
- OSI model and protocols (htp, smb, ftp, ssh, dns)
- Vulnerability scanning (nmap, google, whois, dig)
- Scripting (bash, python)
- Cryptography foundations (encoding, encrypion, hashing)
- Forensic arifacs (logs, system data)

<br>

## OFFENSE IS MORE FUN
1. You need passion
2. You need to be a life-long learner
3. Gamification helps develop life-long learners
4. Offensive Cybersecurity is better gamification
5. Offensive techniques develop a better security mindset
6. Offense is not harder than defense (at an intro. level)

<br>

## BLUE TEAM: STORYTELLING
- Defense is all about stories
- What questions to ask?
- When to ask those questions?
- How do we answer those questions?
- What story is the evidence telling?
- Who needs to hear this story?
- What story do I tell this person?

<br>

## BLUE TEAM: NIST CYBERSECURITY FRAMEWORK
    Idenify -> Protect -> Detect -> Respond -> Recover

1. `Identify`: Develop an organizational understanding to manage cybersecurity rish to systems, people, assets, data, and capabilities.
    - What is inside/outside your organization? Who are the actors? What assets do you have? How do you model your threats?
2. `Protect`: Develop and implement appropriate safeguards to ensure delivery to critical services.
    - How do you secure systems? How do you configure and read logging? What tools and technologies can you leverage? How do lock down network, access controls, mobile, and cloud?
3. `Detect`: Develop and implement appropriate activities to identify the occurence of a cybersecurity event.
    - Now that your defenses were breached, how do you catch the attackers? What do these logs mean; what's normal vs. anomalous behavior? What are indicators of compromise? Is this activity related to security or privacy? What is the timeline of events? How do you link different types of logs together? What are typical attacker tools, tactics, and procedures?
4. `Respond`: Develop and implement appropriate activites to take action regarding a detected cybersecurity incident.
    - How do you manage a security incident? How do you react to live attackers? Who needs to be notified and when? How do you collec forensic evidence that is admissible? How do you build a legal case? What goes into an incident report?
5. `Recover`: Develop and implement appropriate activites to maintain plans for resilience and to restore any capabilities or services that were impaired due to a cybersecurity incident.
    - How do you recover from a security incident? What is a postmortem? How do you secure your systems for the next attack? Why create a bug bounty program?

<br>

## FUNDAMENTALS: CIA
- `Confidentiality`
    - Is this private?
- `Integrity`
    - Is this real?
-  `Availability`
    - Is this usable?

<br>

## FUNDAMENTALS: AAA
- `Authentication`
    - Who are you?
- `Authorization`
    - What can you do?
- `Accounting`
    - Did you do this?

<br>

## FUNDAMENTALS: RISK
- Vulnerability = Weakness
- Threat = a way some weakness(es) might be attacked
- Risk = combination of vulnerabilties and threats
    - Includes likelihoods
- `Vulnerabilities * Threats = Risk`

<br>

## GRC
- `Governance`: The means by which an organizaion is directed and controlled. In GRC, governance is necessary for setting direction (through strategy and policy), monitoring performance and controls, and evaluating outcomes.
- `Risk`: A possible event that could cause harm or loss it more difficul to achieve objectives. In GRC, risk management ensures that the organiation identifies, analyses, and controls risk that can derail the achievement of strategic objectives.
- `Compliance`: The act of ensuring that a standard or set guidelines is followed, or that proper, consistent accounting or other practices are being employed. In GRC, compliance ensures that depending on the context, the organization takes measures and implements controls to assure that compliance requirements are met consistently.