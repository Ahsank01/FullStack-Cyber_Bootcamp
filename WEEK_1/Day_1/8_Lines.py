#!/usr/bin/env python3

"""
Your boss handed you a simple task, just replace the "newlines" from the provided file with spaces... 
(hint - it's not just that simple)
"""

# Import the 'sys' module
import sys

def lines():
    # Get the name of the file from the command line arguments
    file_name = sys.argv[1]

    # Final output string
    output = ''

    # open a file
    with open(file_name, 'r') as f:

        # Iterate over the line
        for lines in f:

            # Remove the newline character from the line
            lines = lines.strip()

            # Append the line to the output string
            output += lines

            # Add a space if the line was not empty
            if len(output) > 0:
                output += ' '

        print(output, end='')

lines()