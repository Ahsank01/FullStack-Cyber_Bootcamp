# Blue Team 09: Incident Response

## OUTLINE
1. What is an `incident`?
2. Incident Response
3. Incident Response Teams
4. Phases of Incident Response

<br>

## WHAT IS AN INCIDENT?
- Event
    - Any obserable occurrence in a system or network
- Adverse Event
    - Any Ecent that has negative consequences
- Security/Privacy Event
    - Any Event that releates to a security/privacy function (CIA, AAA, etc)
- Security/Privacy Incident
    - A violation of security/privacy policies or practices

<br>

## INCIDENT RESPONSE TEAMS (CSIRT)
- Incident Management Team Lead
- Security Analysts 
- Information Technology (IT) admins
- Legal
- PR

<br>

## PHASES: PREPARATION
- Encompasses Identify & Protect
- Creating organizational policies
- Creating CSIRT
    - Staff members & Authority
    - Parnter teams (legal, PR, etc)
- Hardware, software, information required  
    - Forensics (hardwarem bootable images, backup/cloning devices)
    - Logging/monitoring and alerting systems
    - Procedures and playbooks - training
    - Continous Improvement
- Profile `normal` behaviors
- Understand `expected` behaviors
- Establish logging policies
- Synchronize clocks!
- Maintain organization knowledge base
    - Asset inventories!

<br>

## PHASES: DETECTION & ANALYSIS
- Encompasses Detect
- Validate Event -> Incident
- Where do we get Detection Indicators?
    - Alerts, Logs, Public Info, People, Threat Intel.
- Start finding context and stories
- Perform event correclatiion to combine sources
    - SIEM
- Captire network traffic or other evidence
    - This is expensive, both in storage and bandwidth
- Filter information/noise
- Escalate! (seek assistance from internal/external resources)

<br>

## PHASES: CONTAINMENT, ERADICTION, AND RECOVERY
- Encompasses Respond and Recover
- Escalated a detection into an incident!
- Choose and implement a containment strategy
    - Tradeoffs between C - I - A; acting too early vs too late
- Gather more (legal) evidence
    - Know all of the things that happened
- Identify attackers (actors, systems, infrastructure)
- Eradicate the incident
- Recover normal business operations

<br>

## PHASES: POST-INCIDENT ACTIVITY
- Lessons learned review
    - Reports and meetings
- Evidence Retention
- Go back and fix the preparation!

<br>

## SUMMARY
1. Definitions of event, incident
2. Incident response phases and teams
    1. Preparation
    2. Detection & Analysis
    3. Containment, Eradiction, & Recovery
    4. Post-Incident Activities