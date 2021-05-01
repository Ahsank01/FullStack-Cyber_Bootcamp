#!/usr/bin/env python3

'''
Connect to the server and get the key. Couldn't be any simpler.
Test server located at listen.runcode.ninja:9006
'''

# Import 'sys' module to process command line arguments
import sys
# Import 'socket' module to make network connections
import socket


def main():
    # Variables for connection info
    HOST = sys.argv[1]
    # Convert the second argumment to a number. All 'argv' elements are strings
    PORT = int(sys.argv[2])

    flag = ''
    # Index of the character we are requesting
    index = 0

    while not flag.endswith('}'):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            # Receive the initial prompt - i.e. "What do you want?"
            s.recv(1024)

            # Send the 'givechar' command to the application
            s.send(f'givechar {str(index)}\n'.encode())
            # Remove the newline from the response before appending to flag
            char = s.recv(1024).decode().strip()
            flag += char

        # Increment the index to get the next character in the string
        index += 1

    print(flag)


if __name__ == '__main__':
    main()
