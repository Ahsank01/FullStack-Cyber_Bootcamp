#!/usr/bin/env python3

"""
Write a program that will read text file from the command line and determine if the numbers are even or odd.

"""

import sys

def Even_Odd():
    # store a file name in this variable
    file_name = sys.argv[1]

    # open a file. with => this will automatically close the file
    with open(file_name, 'r') as f:
        # read the data line by line, convert it into a list and save it in tha data variable
        data = f.read().split()

        # loop over the data list and pass each value to nums, one at a time
        for nums in data:
            # type cast the nums to an integer and check if its even or odd
            if int(nums) % 2 == 0:
                print(nums, 'True')
            else:
                print(nums, 'False')

Even_Odd()