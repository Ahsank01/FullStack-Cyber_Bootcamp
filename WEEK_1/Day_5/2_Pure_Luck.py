#!/usr/bin/env python3

'''
Connect to the server and guess the lucky number to get a flag!
Test server located at listen.runcode.ninja:9009
'''

# Import 'sys' module to process command line arguments
import sys

# Import 'socket' module to make network connections
import socket


def pure_luck():

    # Variables for connection info
    HOST = sys.argv[1]

    # Convert the second argumment to a number. All 'argv' elements are strings
    PORT = int(sys.argv[2])

    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the host and port provided
        s.connect((HOST, PORT))

        # Receive the response and save it to prompt
        prompt = s.recv(1024)

        # Decode the response and strip it
        prompt = prompt.decode().strip()

        # Set a boolean for the while loop
        flag_not_found = True

        # Counter to increment the loop
        counter = 0

        while flag_not_found:

            # Convert the counter to a string and save it to guess
            guess = f'{str(counter)}\n'

            # Send the response with the guess input
            s.send(guess.encode())

            # Receive the response and decode it
            response = s.recv(1024).decode().strip()

            # Check if the response shows the flag, if not then add one to the counter.
            if response == prompt:
                counter += 1
            else:
                # If flag is found, break the loop
                flag_not_found = False
                print(response)

