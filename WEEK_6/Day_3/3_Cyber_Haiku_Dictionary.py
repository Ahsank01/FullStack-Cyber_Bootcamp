#!/usr/bin/env python3

"""
Someone dropped our cyber haiku dictionary and the order in which they were stored is all messed up. 
Can you fix the order dictionary and print them out in the right order?
"""

# Import 'sys' module to process command line arguments
import sys

# The ast.literal_eval() is an inbuilt Python library function used to convert string to dict.
import ast

# reads in a file and return the data
def cyber_haiku():

    # store a file name here
    file_name = sys.argv[1]

    # open a file in a read mode
    with open(file_name, 'r') as f:

        # read the entire text of a file
        data = f.read()

        # conver the string into a dictionary
        data_dict = ast.literal_eval(data)

        # stores word on the current line
        line = []

        # Iterates through the dictionary after sorting the keys as integers
        for key in sorted(data_dict, key=int):
            word = data_dict[key]

            if word == '\n':
                # If the current word is a newline, print the words in the line
                # separated by a space, and then clear all words from the line.
                print(' '.join(line))
                line = []
            else:
                line.append(word)

cyber_haiku()