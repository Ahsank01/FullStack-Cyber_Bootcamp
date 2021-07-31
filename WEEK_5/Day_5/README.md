# Blue Team 05: Splunk Basics

## SIEM
1. SIEM
2. Security Data Collection
3. Data Normalization
4. Event Log and syslog

<br>

## SIEM
- Log review
- SIEM
    - Need to log relevant events and filter noise
    - Establish scope of events
    - Develop use cases to define a threat
    - Plan incident response
    - Ticketing system
    - Threat hunting

<br>

## SIEM SOLUTIONS
1. Splunk
2. ELK/Elastic Stack
3. ArcSight
4. Exabeam
5. Qradar
6. Alien Vault and OSSIM

<br>

## SECURITY DATA COLLECTION
- Intelligence needs to be current
- SIEMs can be configured to automatically collect
    - What do we want to collect?
    - Data must be stored, processed, and normalized. This has a cost.
- False negatives/positives
    - Develop a use case for behaviors

<br>

## DATA NORMALIZATION
- Security data comes from numerous sources
- What is normalization?
    - Process where data is reformed in an effot to facilitate efficient scanning and analysis
- Where does SIEM data come from?
    - Agent-based
    - Listener
    - Sensors

<br>

## DATA NORMALIZATION
- What is the problem?
    - Proprietary formats
    - Comma-separate
    - Tab-separated
    - XML
    - JSON
    - Text-based
    - Syslog
    - SNMP
    - AND TIME!
    - AND SECURE THE LOGS THEMSELVES!

<br>

## EVENT LOGS AND SYSLOG
- What are event logs?
    - Logs created by the OS on each client/server to record how users and software interact with system
    - Generally provide the name, details of errors, event ID, source of the event and a description
- Syslog
    - Protocol enabling different appliances and software to transmit logs to a central server.

<br>

## SUMMARY
1. Single place to do our log analysis/collection
2. Daa must be normalized to be efficiently analyzed
3. Splunk is one such SIEM solution