#!/usr/bin/env python3

"""
Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. 
However, if the string length is less than 2, return instead the empty string.
"""

import sys

def both_ends():
    # save the first input from the command line argument to the variable word
    word = sys.argv[1]

    # save the sliced word in this variable
    sliced_word = ''

    # check if the length of the word is greater than 2
    if len(word) >= 2:
        sliced_word = word[0:2] + word[-2:]
        print(sliced_word)
    else:
        print()

both_ends()
