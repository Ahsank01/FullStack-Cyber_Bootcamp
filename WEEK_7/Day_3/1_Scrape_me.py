#!/usr/bin/env python3

# import sys library to use command line input
import sys

# import requests library to use a get request
import requests

# save the URL in this variable
URL = sys.argv[1]

# make a get request on the URL
response = requests.get(URL)

# print the response using .text method.
print(response.text)