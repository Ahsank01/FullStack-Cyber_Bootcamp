# Essentials 02: Networking and the Internet
<br/>

## Clients Vs. Servers
---
- `Clients` make requests  
    - Our browser gives us this capability through our url bar.
    - `curl` command is also an http client!
- `Servers` generate responses  
    - Servers interpret the request that is made and generate an appropriate response.
    - Often times, these responses include all of the content necessary to render our web browser.

```
I as a client will make a REQUEST to Google, to look for Facebook.com, and then the google server will RESPONSE be back with the Facebook.com Web Page.
```
<br/>

## Rendering a Webpage
---
- We need three major pieces to render a web page  
    - The actual content of the webpage - HTML
    - The layout/styling of a webpage - CSS
    - The log of a webpage - JavaScript

<br/>

## The Internet - Takeaways
---
- Generally, basic communication over the internet relies on...  
    - A `client` making a `request`
    - A `server` making a `response`
- The three required pieces of information for out browser to render a webpage are  
    - HTML - Content
    - CSS - Styles
    - JavaScript - Logic/Interactivity

<br/>

# LINUX HTTP COMMANDS  
    curl example.com => Make an HTTP request to example.com

    wget example.com => Fetch and download resource from example.com

<br/>

# LINUX DNS COMMANDS
    host host.example.com => Query DNS for records belonging to host

    dig host.example.com => Query DNS for records and information regarding DNS servers

    nslookup host.example.com => Query DNS for IP address belonging to host.example.com
