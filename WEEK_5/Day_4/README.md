# Blue Team 04: Intro to Logs

## OUTLINE
1. Detection
2. What are Logs
3. Why use/collect Logs
4. How to read Logs

<br>

## DETECTION: QUESTIONS
- Defenses have been breached!
- How do you catch the attackers?
- What do these logs mean?
- What's normal vs. anomaluous behavior?
- What are indicators of compromise?
- Is this activity related to security or privacy?
- What is the timeline of events?
- How do you link different types of logs together?
- What are typical attacker tools, tactics, and procedures?

<br>

## DETECTION: STORIES
- Start with an alert, or single indicator of compromise
- Create hypotheses about what could explain it
- Gather additional context and evidence
- Revice hypotheses
- Document everything!
- Write conclusions and cite supporting evidence

<br>

## LOGS: WHAT ARE THEY?
- An official record of ecents
    - Came from ships and aircraft
- Log files contain (semi) structured data about what happened
- Timestamp & Message
    - Actors, actions, errors
- Types of logs
    - Network, Host, Applications, Physical

<br>

## LOGS: WHY COLLECT THEM?
- CIA, AAA
- Non-repudiation
    - Actors cannot refuse actions taken
- Accounting
    - Tracking who, when, and what resources
- Laws!
    - Data retention laws and policies
- Historical record - we may get new information

<br>

## LOGS: HOW TO READ THEM
- Determine what sort of system created these logs
    - Network, Host, Application, Physical, Access, etc
    - Narrow this down as much as possible - use context clues
- Map out the structure
    - Timestamp, message, delimiters, fields
    - Is each line separate, or are groups of lines for a single log message?
- Identify additional related info
    - Network models, operating systems, types of applications
- Parse content
    - What is the story that the logs are telling

<br>

## INTERLUDE: TIME
- Timestamps can be formatted differently!
- Linux Epoch
    - Number of seconds since Jan 1, 1970
- GMT & UTC
    - Greenwich Mean Time
    - Coordinated Universal Time
- Time zones

## SUMMARY
1. Detection is about stories
2. Hyptotheses -> Evidence -> Revise -> Conclusions
3. Logs! Collect all the logs!
4. Reading new logs