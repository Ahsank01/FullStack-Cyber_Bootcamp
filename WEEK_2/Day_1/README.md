# Essentials 06: Data Encoding and Cryptography
<br/>

## Encoding - Hide and seek for binary
---
1. ASCII
2. UTF8
3. HEX
4. Base 64
5. URL encoding

<br/>

### Encoding
---
- To convert data from one format to another
- Not inherently a security concept
- The most important part of encoding is that our `scheme` is standardized
- At the bottom line all data must be represented by `1s` and `0s`

<br/>

### Data in Bits
---
- Instead of our decimal system where you can count from `binary 0-9` in any columns of data, you can only count from `0-1`

<br/>

### The Math You Know
```
                        9
                    +   9
                    ------
                       18
                  0101 0100
```

<br/>

### Base 64
---
- `Base64` is designed to carry data stored in `binary` formats across channels that only reliably support text content.
- Can be used on the `web` to embed image files or other binary assets inside `HTML` and `CSS` files

<br/>

## Cryptography
---
- Encryption
    - Types of Encryption
    - Common Encryption Methods
- Hashing and Password Security

<br/>

### Encryption
---
- Hiding a message using the power of `MATH`
- Used for communication between parties where secrecy is of the utmost importance
- The hidden message, `cipher`, should be able to be shown to anyone without revealing the actual `encryption`
- `Encryption is a reversible process`
```
    plaintext       scheme      ciphertext
    ---------       -------     -----------
      word          encrypt       981kje
                    ------>
                      key
                    <------
                    decrypt
```

<br/>

### Types of Encryption
---
1. `Symmetric Encryption`: Both parties have a copy of the same key
2. `Asymmetric (Public) Key Encryption`: There is one key for locking the safe and one key for opening it

<br/>

### Key Generation Requirements
---
1. There must be both a `public key` and a `private key`
2. The `public key` can be given to anyone and allows anyone to `lock` things up for you
3. The `private key` is your own.

<br/>

### Asymmetric Encryption Implications
---
    1. Confidentiality: If someone encrypts a message for me using my public key, I can decrypt that message
    2. Integrity: If I encrypt a message with my private key, people can't decrypt it with my public key

<br/>

### Hashing
- Hiding a message using the power of Math.
- Used for storage and/or verification of `data`
- Finding a particular `hash` should tell you nothing about the original data.
- `Hashing is an irreversible process`

<br/>

## Authentication and Cookies
---
- HTTP
- Authentication
- Cookies and Sessions

<br/>

### HTTP
---
- An `application-level` communications protocol.
- Specifies allowable `metadata` and `conetn` of messages.
- Does `NOT` specify how messages are transmitted!
- `STATELESS`: does not remember the previous request/response cycle!

<br/>

### AAA
        Authetication
            "This person is who they say they are"

        Authorization
            "This person is allowed to do X, Y, Z"

        Accounting
            "Who the heck is using all our bandwidth?"

<br/>

### COOKIES & SESSIONS
```
No need to authenticate for every request
```

<br/>

## Braindump on HTTP/s
---
1. `Not Secure` - Data being sent over is `not encrypted`
2. `STATELESS` - HTTP does not remember anything!!!  
    - So how do we remember things?  
        => Cookies
3. Usually get responses with HTML, CSS and JavaScript
4. Responses have response codes!  
    - 2XX = ALL OK!
    - 3XX = Some kind of redirect
    - 4XX = Some kind of client error
    - 5XX = Some kind of server error
5. Requests have `headers`
    - `User-Agent` - What kind of browser the client is
    - `Host` - The host you are making the rewquest to
    - `Cookie` - Additional data sent so the server can remember the client
6. Request have `verbs`  
    - `GET` - Give me a resource - NO BODY IN GET REQUEST
    - `POST` - I would like to create a resource on the server - usually has a body `data to send to create something`
    - `PUT` - Would like to update a resource on the server
    - 'DELETE` - Would like to delete a resource on the server
