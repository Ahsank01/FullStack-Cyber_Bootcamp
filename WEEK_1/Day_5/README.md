# Essentials 05: Python Sockets
<br/>

## What are Sockets?
---
1. Endpoint for communication between two proocesses (similar to `nc`)
2. Most often used for communication between two different `nodes` on a `network`, but can be used for processes on the same machine
3. A way to `automate` some of the process that otherwise may be tedious with `nc`

<br/>

## Sockets in Python
---
- The `socket` module is part of Python's standard library.
```python
import soceket
```
- `Sockets` are made up of two parts  
    - IP address
    - Port
    - Provided as a tuple
    - Tuples are `immutable` ordered collections
    - The way we sen them as a `tuple` is by using `double parentheses`

<br/>

## Socket Process
---
- First we need to import the `socket` library
```python
import socket
```
- Then we need to import the `sys` library so we can take in `arguements`
```python
import sys
```
- Next, we use the `sys` library to get our `HOST` information
```python
HOST = sys.argv[1]
```
- We do the same to get our `PORT`, except we also cast it to an int
```python
PORT = int(sys.argv[2])
```
- We create the socket with the built-in function
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
```
- We connect to the `HOST` & `PORT` provided on the command line
```python
s.connect((HOST,PORT))
```
- Receive response from the connection in the first 1024 bytes.
```python
data = s.recv(1024)
```
- Decode the received data
```python
decoded_data = data.decode()
```


<br/>

### General Rules
- Solve with `nc` first
- Don't be afraid to reuse code
- `Commenting` is crucial part of learning