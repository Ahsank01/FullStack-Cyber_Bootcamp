# Red Team 02: Passive Information Gathering

## Outline
---
- Definition
- Tools
    - `Google`
    - `theHarvester`
    - `whois`
    - `netcraft`
    - `recon-ng`
- Summary

## Passive Reconnaissance
---
Passive reconnaissance is an attempt to gain informtion about targeted computers and networks withour actively engaging with the systems.

<br/>

### Google Hacking
---
        Filter                  Meaning
          ||                      ||
          \/                      \/
        site:                 Results on this site
        filetype:             Results with this file-type
        inurl:                Results with this term in the url
        intitle:              Results with this term in the title
    -----------------------------------------------------------

        Operators               Meaning
           ||                     ||
           \/                     \/
        - FILTER_OR_TERM        Exclude this
        (FILTERS_OR_TERMS)      Group these filters and/or therms
        FILTER | FILTER         Results for this or this. Note you can only use OR instead of |
        FILTER AND FILTER       Results that meet both this and this

<br/>

### theHarvester
---
1. Finding emails from an organization can be critical in finding a target for an exploit who may be viewing your email on the internals of the network.
2. Open source tool pre-installed in Kali for acquiring emails from differnt major resources is `theHarvester`

<br/>

### whois
---
1. Domain registration often requires you to provide a lot of information about ownership regarding a domain name.
2. This creates a track record of ownership, which is great for disputes.
3. This information includes registrar, name server and, sometimes, full contact information.

<br/>

### netcraft
---
- A website that hordes a wide variety of information regarding any particular website.
- This information includes all different types of information pertaining to general background, networking, DNS, tracking information, content distribution network (CDNs), content management systems (CMS), and more!

<br/>

### recong-ng
---
- A recon tool that can be used for both passice and active recon.
- To install all modules run `marketplace install all`