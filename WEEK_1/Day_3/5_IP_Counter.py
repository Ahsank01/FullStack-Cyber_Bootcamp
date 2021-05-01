#!/usr/bin/env python3

"""
You are asked to take a look at an apache log file and count the occurrences of each unique ip address in the file -
to see where the traffic is coming from. 
In terms of sorting, just sort them in lexicograhical order (sort the IP strings).
"""


import sys

def IP():
    # store a file name here
    file_name = sys.argv[1]

    # store the IP and its count here
    IP = {}

    # Open a file
    with open(file_name, 'r') as f:

        # loop over the data
        for line in f:
            # split the line into a list
            IP_List = line.split()
            # pick the first item from the list and store it to a variable ip_addr
            ip_addr = IP_List[0]

            # check if the IP is already in the dictionary
            if ip_addr in IP:
                # add one to the value if TRUE
                IP[ip_addr] += 1
            else:
                # otherwise add the IP to the dictionary and give it a value = 1
                IP[ip_addr] = 1

        # sort the dictionary and print it
        for ip_addr in sorted(IP.keys()):
            print(f'{ip_addr} - {IP[ip_addr]}')

IP()