# Blue Team 07: Defense in Depth

## OUTLINE
1. Indicators of Compromise
2. Detecting Attacks
3. Network Detections
4. Host Detections
5. Application Detections

<br>

## INDICATORS OF COMPROMISE
- Evidence left behind by attacks
- Logs
    - Requests made, errors, actions taken
- Artifacts
    - User accounts, services, machines
- Metrics
    - Service degradation, strange activity upticks, failure rates

<br>

## DETECTING ATTACKS
- How do we know we've been breached?
    - Alerts, anomly detection, reports, attackers, service issues
- Get report - investigation issue!
    - Hypotheses <> Evidence
    - Conclusions with Reasoning and supporting Evidence

<br>

## NETWORK DETECTIONS
- Where and what logs are we collecting?
    - Routers - Netflow, RMON, SNMP
    - Scanners - ping, iPerf, network mapping
    - Network taps - pcap, other analyses
    - Firewalls - dropped vs allowed packets
- Where are alerts coming from?
    - Network defenses!
    - NIDS, monitoring thresholds and tools, humans
- Types of network issues and attacks
    - Scans/probes, DoS, rogue devices, link failures, beaconing
- How do we triage and deal with these issues?
    - Use tools - they help identify and prioritize alerts
    - IPS - block/drop traffic
    - Third-party providers - sinkhole traffic from DoS
    - Use network maps to identify what is working
    - Think about CIA - is this even a security issue?

<br>

## Host Detections
- Where and what logs are we collecting?
    - On the hosts!
    - System resources, software/apps, access/privilege
    - Monitoring tools
    - Windows - perfmon, resmon, sysinternals
    - Linux - `ps, top, df, w`
- Where are alerts coming from?
    - SCCM - central logging tools
    - AV, authentication/access logs

<br>

##  APPLICATION DETECTIONS
- Where and what logs are we collecting?
    - Service status, failures, actions
- What type of events or alerts should we catch?
    - Anomalous activity
    - New accounts - AAA
    - Unexpected output
    - Unexpected outbound communications (networks!)
    - Service interruptions
    - Memory overflows

<br>

## SUMMARY
1. Indicators of Compromise - evidence/alerts
2. Detecting and dealing with attacks/issues
    1. Networks
    2. Hosts
    3. Applications