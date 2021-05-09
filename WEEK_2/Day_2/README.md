# **Essentials 07: HTTP**
<br/>

## Authentication and Cookies
- HTTP
- Authentication
- Cookies and Sessions

<br/>

## HTTP
---
- An `application-level` communications protocol.
- Specifies allowable `metadata` and `conetn` of messages.
- Does `NOT` specify how messages are transmitted!
- `STATELESS`: does not remember the previous request/response cycle!

<br/>

## AAA
        Authetication
            "This person is who they say they are"

        Authorization
            "This person is allowed to do X, Y, Z"

        Accounting
            "Who the heck is using all our bandwidth?"

<br/>

## COOKIES & SESSIONS
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
    - `DELETE` - Would like to delete a resource on the server
    - `PATCH` - To partially update data at a resource
