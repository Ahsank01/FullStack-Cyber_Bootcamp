#!/usr/bin/env python3

"""
We will work progressively solving a problem and modifying our code to meet new requirements. 
Our end goal is to write a script which can take in a user supplied input file -
and count the total number of times the word 'quack' is found in the file.
"""

# Import the 'sys' module
import sys

def main():
    data = parse_file()
    count_quacks(data)

# this function will read a file name from the the command line arguements -
# using the sys.argv[1], and will return the data as a string
def parse_file():

    # open a file
    with open(sys.argv[1], 'r') as f:

        # read the whole file using the .read()
        data = f.read()
        
        # return the content stored in data
        return data

# this function will count the appearence of quack
def count_quacks(s):

    # split the data into a list.
    data = s.split()

    # variable to keep track on quack count
    count = 0

    # loop over the list
    for word in data:
        # look for a word quack
        if word == 'quack':
            # add 1 to count if True
            count +=1
    print(count)

main()
