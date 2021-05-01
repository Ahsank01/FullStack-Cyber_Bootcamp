#!/usr/bin/env python3

"""
The path to the input file will be passed into your program as a command line argument when your program is called.
Write a program that receives a single word as input and checks to see if the word is a palindrome 
(i.e. words that look the same written backwards).
"""

import sys

def F_is_B():
    # store a file name in this variable
    file_name = sys.argv[1]

    # open a file. with => this will automatically close the file
    with open(file_name, 'r') as f:
        # read the data line by line, convert it into a list and save it in tha data variable
        data = f.read().split()

        # loop over the data list and pass each value to words, one at a time
        for words in data:
            # check if the word is a palindrome
            if words == words[::-1]:
                print("True")
            else:
                print("False")
F_is_B()