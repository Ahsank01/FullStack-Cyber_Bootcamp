# Blue Team 03: Firewalls & IDS

## OUTLINE
1. Intrusion Detection/Prevention Systems
2. Snort
3. Snort Rules

<br>

## Intrusion Detection/Prevention Systems
- IDS/IPS - almsot interchangeable
- Actions: Allow, Deny, Alert
- Network-Based vs Host-Based
- Deeper packet inspection
    - Trade-offs with resource usage
- Detection
    - Signatures
    - Anomalies

<br>

## SNORT
- Network Intrusion Detection System
- Inspect packets over a network and make decisions
    - Alert
- Signature bases
- Rule vs heuristics
    - Thresholds can still be rule-based

<br>

## SNORT RULES
Basic outline of a snort rule
    [action][protocol][sourceIP][sourceport] -> [destIP][destport] ([Rule Options])

- Always start with the 5-Tuple
    - Source IP, source port, destination IP, destination port, protocol
    - The direction will generally be source -> destination
    - May be 'any'
- Rule Options
    - sid = unique identifier, use large numbers (>1,000,000)
    - msg = human-readable message
    - Others: flags, thresholds, packet bytes, etc.

## SUMMARY
1. IPS/IDS
2. Snort Architecture
3. Snort Rules