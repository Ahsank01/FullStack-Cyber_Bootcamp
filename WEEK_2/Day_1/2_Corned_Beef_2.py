#!/usr/bin/env python3

# Import 'sha512' function from 'hashlib' module
from hashlib import sha512

flag_hash = "a497453fe1eee3e0c4d44f2a74a1518744d247a1c6dd6c902a2b3367987f0e5d21fb1cbdd1af55ea78098be5a336ffaf06f19b8e5a5997e06d20ce00f9907424"

# Iterate over hex numbers from 0 - FFF
for num in range(4096):
    # Zero pad the number uppercase and lowercase
    padded_numbers = [f'{num:03x}', f'{num:03X}']
    print(padded_numbers)
    for hex_num in padded_numbers:
        flag = f'FS{{hash-I_had_corned_beef_and_hash_{hex_num}}}'
        guess = sha512(flag.encode())
        # print(hex_num)
        # print(guess.hexdigest())

        if guess.hexdigest() == flag_hash:
            print(flag)
            print(hex_num)
            print(guess.hexdigest())
            exit(0)