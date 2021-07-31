# Essentials 03: Python Data Structures
<br/>

### Collection Data Types
---
- List  
    - Ordered collection of data
- Tuple  
    - Immutable ordered collection of data
- Set  
    - Unordered collection of unique items
- Dictionary  
    - An unordered set of key-value pairs

<br/>

#### Difference between List and Dictionary
    - List elements are accessed via indexing
    - Dictionary elements are accessed via keys

#### Commanality between List and Dictionary
    - Mutable
    - Dynamic
    - Both can be nested

#### Python Lists
```python
List = ['Alice', 'Bob', 'Carl']
           0       1       2
```

#### Python Dictionary
```python
Dictionary = {
    'Colorado' => 'Rockies',
    'Boston' => 'Red Sox',
    'Seattle' => 'Mariners',
}
```
<br/>

## Python Dictionaries
---
```python
Creating dictionaries

my_dict1 = {}

my_dict2 = {'Name':'Albert', 'Age':99}
```
```python
Getting a value

print(my_dict2['Name'])

years = 'Age'

print(my_dict[years])
```
```python
Adding key/value pais

my_dict1['fruit'] = 'banana'
my_dict1['meaning of life'] = 42
```
```python
Updating value

my_dict1['fruit'] = 'apple'
```
```python
Test for key

print('fruit' in my_dict1)
output => True

print(42 in my_dict1)
output => True
```
```python
Deleting key/value

del my_dict2['Age']
print(my_dict2)

output => {'Name':'Albert'}
```
```python
Looping over a dictionary

# k => heys
# v => values

for k in my_dict1:
    print(k, my_dict1[k])
    # Key, Value of [k]

for k in my_dict1.keys():
    print(k)
    # prints only the keys

for v in my_dict1.values():
    print(v)
    # prints only the values

for k, v in my_dict1.items():
    print(k, v)
    # prints the key and its value
```
