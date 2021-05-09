#!/usr/bin/env python3

from base64 import b64decode

enc_str = "25c6e4734623866785234757a5854666467486073613933326336537a56493e6a585256636239366a57465c636648377f44454a7258403d3"

# reverse the hex string
rev_enc_str = enc_str[::-1]

# decode the hex string
base64_str = bytes.fromhex(rev_enc_str)

# reverse the base64 string
rev_base64_str = base64_str[::-1]

# decode the base64 string and print the flag
print(b64decode(rev_base64_str).decode())