#!/usr/bin/env python3

"""
Santa has asked if you can help him parse his list naughty or nice list of people for his upcoming christmas delivery. 
It looks as though the elves that were writing down the names of those naughty or nice didn't keep the same format. 
Can you give santa a total count of how many nice and how many naughty people are on his list?
"""

import sys 
import ast

def main():
    # Get the filename passed to
    filename = sys.argv[1]

    # Create a dictionary to hold the naughty/nice counts
    count = {}
    count['good'] = 0
    count['bad'] = 0

    # Open the file for reading
    with open(filename, 'r') as f:
        # iterate over each line of the file
        for line in f:
            line = line.strip()

            # get all words from the line
            words = line.split()

            # get the last word of each line
            status = words[-1]

            # Increment the counts
            count[status] += 1

    # Print the final output
    print(f'Naughty list has {count["bad"]} people!')
    print(f'Nice list has {count["good"]} people!')

main()