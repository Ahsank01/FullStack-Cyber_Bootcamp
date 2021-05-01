#!/usr/bin/env python3

"""
Given a list of strings, return the count of the number of strings where the string length is 2 or more 
and the first and last chars of the string are the same.
Note: python does not have a ++ operator, but += works.
"""

import sys

def match_ends():
    # use [1:] to read all the values, not just the first one
    List = sys.argv[1:]

    # to count the number of words that matches the requirements
    count = 0

    # loop over the inputs came from the command line arguments
    for word in List:
        # check if the length is >= 2 and if the first and last index are the same
        if len(word) >= 2 and word[0] == word[-1]:
            # add 1 to count, each time the above statements is True
            count += 1
        else:
            pass

    print(count)

match_ends()