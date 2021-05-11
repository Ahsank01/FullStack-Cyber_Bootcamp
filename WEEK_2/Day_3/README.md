# **Essentials 08: Python Requests**
<br/>

## Review
---
- HTTP Verbs  
    - `GET` -> Read
    - `POST` -> Create
    - `PUT` -> Update
    - `DELETE` -> Delete

- HTTP Status Codes  
    - `200` -> Success
    - `400` -> User Error
    - `500` -> Server Error

<br/>

## Requests
---
```python
import requests

r = requests.get('https://api.github.com')
print(r.status_code)
print(r.headers['content-type'])
```
<br/>

## Using Requests
---
- `GET`  
    - response = requests.get(url)
- `POST`   
    - response = requests.post(url, data)
- `PUT `    
    - response = requests.put(url, data)
- `DELETE`  
    - response = requests.delete(url)

<br/>

## Summary
---
- Using the `requests` module we can interact with websites in `python`
- The `requests` library also allows us to interact with `RESTful APIs`