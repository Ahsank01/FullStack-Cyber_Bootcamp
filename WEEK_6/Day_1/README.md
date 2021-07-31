# Essentials 01: Command Line Arguments and Reading Files
<br>

## Command Line Arguments
---
- import sys => enables a sys library
- The package sys, comes with a lot of things, all defines on sys as as property(some static value) or a method (some function that directly uses sys).
- Use sys.argv[] property to pass all the inpurt in during execution.
```console
kali@kali:~$ ./python.py <input>
```
<br>

## Reading Files with Python
---
The `open` function creates an object that you can use to interact with files.

The first argument to open is the name of the file you want to read. The second argument to open is the mode you want when opening the file.
To open a file for reading, use the string `'r'`.
```python
f = open(file_name, 'r')
```
The `f` variable can now be used to read the contents of the file. To read the entire contents of the file at one time, use the `read` method.
```python
f = open(file_name, 'r')
file_contents = f.read()
```
If you want to read the contents of the file one line at a time, you can use the `readlines` method to create a list containing each line of the file as an element.
```python
f = open(file_name, 'r')
file_contents = f.readlines()
```
You can use the `with` keyword along with open to automatically close the file when the block ends.
```python
with open(file_name, 'r') as f:
    for line in f:
        #do stuff
```
When you are processing a file be mindful of the non-printing characters, specifically, the new line character `\n`. Each line in a file will be terminated with the new line character (windows uses `\r\r\n`). There are a few ways to deal with the new line character.

You can use the `splitlines()` method after using the read function, create a list of each line withour the new line character.
```python
with open(file_name, 'r') as f:
    file_contents = f.read().splitlines()
```
Alternatively you can use the `strip` function to remove the new line character at the end of each line.
```python
with open(file_name, 'r') as f:
    for line in f:
        line = line.strip()
```