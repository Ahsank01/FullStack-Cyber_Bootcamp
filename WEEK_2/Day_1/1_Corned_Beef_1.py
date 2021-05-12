#!/usr/bin/env python3

'''
I can't even remember what I had for breakfast let alone the flag for this problem. 
I know it was something like FS{cabbage-wait_that's_not_right_XXX} where X is a number, 
but I do not remeber exactly what number I used. 
Maybe it was my apartment number or the first three digits of my phone number - 
I just do not know. I do still have the md5 hash though if that helps: 3323c1ae476e81fdc3a7cf3f8b8da6ed
'''

# Import hashlib to use md5 hash
import hashlib

# Actual hash that we have to compare
hash_flag = "3323c1ae476e81fdc3a7cf3f8b8da6ed"

# loop in range of 1-999
for num in range(1,1000):

    # get the actual flag and concatenate with a number, and convert it into a string
    flag = "FS{cabbage-wait_that's_not_right_" + str(num) + "}"

    # hash the flag in md5 and encode it
    flag = hashlib.md5(flag.encode())

    # save it in a hexdigest mode
    flag = flag.hexdigest() 

    # compare the two hashes
    if flag == hash_flag:

        # print the number that worked
        print("XXX: " + str(num))

        # print the flag
        print("FS{cabbage-wait_that's_not_right_" + str(num) + "}")
        break

