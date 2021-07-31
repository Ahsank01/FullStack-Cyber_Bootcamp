#!/usr/bin/env python3

"""
Given an int count of a number of donuts, return a string of the form 'Number of donuts: [count]', 
where [count] is the number passed in. However, if the count is 10 or more, 
then use the word 'many' instead of the actual count. 
So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'
"""

import sys

def count_donuts():
    # take the number of donuts from the command line and store it in num_of_donuts
    num_of_donuts = sys.argv[1]

    # check if the number is greater than or equal to 10, and print the output accordingly
    if int(num_of_donuts) >= 10:
        print('Number of donuts: Many')
    else:
        print('Number of donuts: ' + num_of_donuts)

count_donuts()