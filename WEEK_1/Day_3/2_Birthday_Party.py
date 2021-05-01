#!/usr/bin/env python3

"""
You've been ordered to print name tags for your friend's birthday party! 
You noticed that quite a few people seem to share the same name at this party -
so you're putting together an organized list for your order. Given a list of names, 
print out the number of occurrences of each name.
"""

# Import the 'sys' module
import sys

# this function will count the names from a file
def count_names():

    # store a file name in this variable
    file_name = sys.argv[1]

    # store a dictionary of the name and its value in this variable
    name_count = {}

    # open a file
    with open(file_name, 'r') as f:

        # read the whole file and split it into a list
        data = f.read().split()

        # loop over the list
        for line in data:

            # erase all the extra white space
            name = line.strip()

            # check if the name is in the dictionary already
            if name in name_count:

                # if yes? add one to the value
                name_count[name] += 1

                # otherwise add a key to the dictionary and assign it a value=1
            else:
                name_count[name] = 1

        # sort the dictionary and print the keys and the values
        for k, v in sorted(name_count.items()):
            print(f'{k} - {v}')

count_names()