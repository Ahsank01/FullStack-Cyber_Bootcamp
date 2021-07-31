#!/usr/bin/env python3

"""
Given a list of strings, return a list with the strings in sorted order, 
except group all the strings that begin with 'x' first. e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
Hint: this can be done by making 2 lists and sorting each of them before combining them.
"""

import sys

def Front_X():
    List = sys.argv[1:]

    # store all the words that starts with 'x'
    new_list_X = []
    # store the rest of the words here
    new_list = []
    # store the final sorted list here
    final_list = []

    # loop over the list
    for word in List:
        # check if the first index of the word is x
        if word[0] == 'x':
            new_list_X.append(word)
        else:
            new_list.append(word)

    # sort the list that does not contain a word starting with x
    new_list = sorted(new_list)
    # sort the list whose words starts with x
    new_list_X = sorted(new_list_X)
    # append the new_list and new_list_X
    final_list = new_list_X + new_list

    print(final_list)

Front_X()
