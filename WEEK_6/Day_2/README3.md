# Blue Team 02: Recon & Assest Management

## OUTLINE
1. Vulnerabilities
2. Vulnerability Scanning
3. Vulnerability Management

<br>

##  VULNERABILITIES ASSESSMENTS
- You must ID your vulnerabilities so that you can mitigate them
- Vulnerability assessments - Use some software that will learn about a system and report back
    - Collect attributes
    - Establish a baseline
    - Look for anomly
    - Report results
- Usually done with automation

<br>

## VULNERABILITIES: SERVERS & APPS
- Missing patches
- Outdated, unsupported systems or applications
- Buffer overflows
- Privilege escalation
- Arbitrary code execution
- Insecure protocols
- Debug information
- Injection, CSS, CSRF, etc.

<br>

## VULNERABILITIES: NETWORK
- Non-patched Firmware updates
- Outdated ciphers (SSL/TSL)
    - Don't use SSL. Use TLS 1.2
- Certificate issues
    - Mismatched names, Expiration, Unknown CA
- DNS
    - Zone transfers! Open resolvers, amplification
- NAT IP exposure
- VPN, SSH, remote desktop

<br>

## VULNERABILITIES: VMs
- VM sandbox escape
- Management interfaces
- Patches, patches, patches
- Virtual guests (see servers); virtual networks (see networks)
    - It is rabbits all the way down!

<br>

## VULNERABILITIES: IoT AND OTHER
- Firmware never gets updates
- Hardcoded passwords (or none)
- Smart power grid
- Microphones and cameras
- Indicatiors of home presence
    - Smart locks/bulbs/alarms

<br>

## VULNERABILITY SCANNING
- Who will conduct the scan
- When will the scan be conducted
- Which systems get scanned
- How will scanning impact the system
- Does the system need to be isolated
- Scanners
    - Nessus, Nikto, OpenVAS, WpScan, etc.
    - Vulneravility reports
- Credentials and Agents
- CVSS
    - CVSS2#AV:N/AC:M/Au:N/C:P/I:N/A:C

<br>

## VULNERABILITY MANAGEMENT: WHY?
- Regulations
    - PCI DSS & FISMA
- Business impacts
    - CIA: limited, serious, servere/catastrophic
- Security & Privcay
    - GDPR
- Internal policies
- External policies

<br>

## VULNERABILITY MANAGEMENT: WHAT?
- The assets we identified!
- Data classifications
    - PII, confidential, IP, etc.
- Business critical 
    - CIA: Limited, Serious, Severe/Catastrophic
- Regulation/contract defined
    - PCI systems, vendor requirements

<br>

## VULNERABILITY MANAGEMENT: HOW?
- Detection -> Testing -> Remediation -> ...
- Prioritization
    - Critically, Difficulty, Severity, Exposure
- Documentation
    - Exceptions, false positives, processes
- Service Level Objectives/Agreements (SLO/SLA)

<br>

## SUMMARY
1. Vulnerabilities can be everywhere
2. Understanding scanning and CVSS
3. Vulnerability Management