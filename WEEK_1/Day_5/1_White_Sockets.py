#!/usr/bin/env python3

# Import 'sys' module to process command line arguments
import sys 

# Import 'socket' module to make network connections
import socket

def socket():
    # Variables for connection info
    HOST = sys.argv[1]

    # Convert the second argumment to a number. All 'argv' elements are strings
    PORT = int(sys.argv[2])

    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # Connect to the host & port provided on the command line
        s.connect((HOST, PORT))
    
        # Receive the first 1024 bytes of data
        data = s.recv(1024)
    
        # Decode and strip the byte string to get the data as a string
        flag = data.decode().strip()

    print(flag)

socket()