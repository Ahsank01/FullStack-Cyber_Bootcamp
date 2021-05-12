#!/usr/bin/env python3

# sys => Collection of command line arguments. We will be using sys.argv[] for this problem.
import sys


def command_line():
    val_1 = sys.argv[1]
    val_2 = sys.argv[2]

    print(val_1) #Ex. 1
    print(type(val_1)) #Ex. 2
    print(val_1 + val_2) #Ex. 3

command_line() 
