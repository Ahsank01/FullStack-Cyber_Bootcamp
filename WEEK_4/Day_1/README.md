# Red Team 06: Web Exploits

## FUNDAMENTAL CONCERNS
- `Authentication` => Trusting that someone is who they say they are.
- `Authorization` => Giving resource access to the right people.
- `Communication` => Transferring data through potentially unreliable middlemen.
- `Control` => Limiting or understanding the capabilities of agents.

<br>

## OWASP TOP 10 (2013)
- `Injection` => Server-side code execution
- `Broke Authentication` => Allows for impersonation
- `XSS` => Client-side code execution
- `Direct References` => Access control can be circumvented
- `Security Misconfiguration` => Vulnerable default/inherit settings
- `Data Exposure` => Data is insecurely transmitted, stored, or simply overshared
- `Missing Access Control` => Users can do things they shouldn't be allowed to do
- `XSRF` => Abuse the target website's trust in the browser
- `Vulnerable Components` => Thirs-party tools are vulnerable
- `Unvalidated Redirects` => Abusable open-ended forwarding

<br>

## UNCOVERING SECRETS
- Assume attacker has access to codebase
- Defense vulnerable if...
    - `application secrets` are easy to discover
    - files are improperly shared
- Bad stuff: app impersonation, decryption

<br>

## IMPROPER ACCESS
- Assume attacker is client
- Defense vulnerable if client can `act outside of authorization`
- Bad stuff: depends on the action and resource
- Frontend `access control` is actually just good `UX`
- True access control comes from backend
- Considerations (be thorough)...
    - Requested resource
    - Reguested action
    - Agent making request

<br>

## INJECTION
- Assume attacker is non-admin client
- Defense vulnerable if client can `execute code on server`
- Bad stuff: umm, everything?

<br>

## REMOTE FILE INCLUSION
- `Step 1`: Attacker injects malicious script to Web Application
- `Step 2`: Malicious code is executred from attacker's website
- `Step 3`: Server downloads malicious file from attacker's website
- `Step 4`: Attacker gets control over the Web Application

<br>

## SQL and SQL INJECTION
---
KEYWORD => ACTION   
SELECT => Which `COLUMNS` to include in output table
FROM => Which `TABLE` to pull data from  
JOIN => Another `TABLE` to glue/concatenate to the output
ON => what `COLUMNS` must match when joining two tables
WHERE => Which `ROWS` to include in the output table

SQL INJECTIONS  
- ' or '1'='1  
- ' or 1='1  
- ' or 1='1  
- 1' or 1=1 -- -
 
<br>

## CROSS-SITE SCRIPTING
### XSS
- Assume attacker is non-admin client
- Defensive vulnerable if can excute code on another client
- Bad stuff: pretty much everything
- Two Flavors: `stored` and `reflected`

### REFLECTED XSS
- Server sends parts of request in response
- Attacker forms a link with the script in it
- Victim clicks the link
- Server responds with the script
- Script runs on the vistim's browser

<br>

## XSRF/CSRF
STEPS:  
1. Perpetrator forges a request for a fund transfer to a website
2. Perpetrator embeds the request into a hyperlink and sends it to visitors who may be logged into to the site
3. A visitor clicks on the link, inadvertently sending the request to the website.
4. Website validates request and transfers funds from the visitor's account to the perpetrator

<br>

## DATA THEFT (BAD AUTH / DATA EXPOSURE)
### IDENTIFY THEFT
- Assume attacker has access to middlemen and database
- Defense vulnerable if communication or storage exposes password
- Bad stuff: user impersonation

### AUTHENTIC SERVER
- Has an SSL ceritificate
- Digitally signed
- Forms a web of trust
- Self-signed in development

<br>

## HTTPS IN PRACTICE
With openssl generate a private key with...
```
$ openssl genrsa -out key.pem 2048
```
Then generate selg-signed SSL certificate with...
```
$ openssl req -x509 -new -nodes -key key.pem -days 1024 -out cert.pem
```
Now use node's https library with this key and certificate

<br>

## SALT
- Random string, unique to each user
- Added before hashing the password
- Two users with the same password with different hashes
- Hashes are not computable ahead of time (unless they know the salt of each user)

<br>

## BROKEN AUTH
- Assume attacker is guest client
- Defense vulnerable if signup or login are improper
- Bad stuff: user impersonation, admin impersonation

<br>

## OVERSHARING
- Assume attacker is non-admin client
- Defense vulnerable if attacker can see sensitive info of another 
- Bad stuff: failed user privacy, NSA loves you

<br>

## GOOD AUTH
- Communication is secure
- Storage is secure
- Cannot set privileges via signup
- Logging in requires username and password
- Data is not inadvertently shared