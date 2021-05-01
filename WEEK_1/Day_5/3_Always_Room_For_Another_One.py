#!/usr/bin/env python3

'''
Connect to the server and follow the directions. Perform to standard and you will get a flag!
'''

# Import 'sys' module to process command line arguments
import sys

# Import 'socket' module to make network connections
import socket

def another_one():
    # Variables for connection info
    HOST = sys.argv[1]

    # Convert the second arguement to an integer
    PORT = int(sys.argv[2])

    # Creata a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        # Connect with the HOST and PORT provided
        s.connect((HOST, PORT))

        # Make a boolean for a while loop
        flag_not_found = True

        # Loop until the flag is not found
        while flag_not_found:

            # Receive the response, decode it, then strip it
            prompt = s.recv(1024).decode().strip()

            # Ignore it if the prompt is empty
            if prompt == '':
                continue

            # If the prompt starts with add 1 to me, add one to it
            if prompt.startswith('add 1 to me:'):

                # Split the prompt into a list, and pick the last index of the list
                number = prompt.split()[-1]

                # Conver the last index of the list to an integer
                number = int(number) + 1

                # Conver the number to a string, and add a newline
                answer = str(number) + '\n'

                # Send the answer as an input, in a decoded form
                s.send(answer.encode())

            # Else flag is found
            else:
                flag_not_found = False
                flag = prompt.split()[-1]
        print(flag)


