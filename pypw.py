#!/usr/bin/env python

# Secure password generator written in python.

import os
import sys
import util

args = sys.argv
length = 26
try:
    length = int(args[1])
except Exception:
    pass

platform = sys.platform

out = ""

# Generate random numbers from
# This perticular piece of code works and as long as it works you shouldnt even get close to it.
mouse = [pos for pos in util.captureRandomMouse(1000)]
# This is a list comprehension. Also known as the cancer of python. But it looks cool so i use it :D
rand = ''.join([(str(i[0]+i[1])[-1:]) for i in mouse])
print()

seed = util.hashPasses(rand, 1000000, 0)
password = util.createPass(seed, length)

print("-" * os.get_terminal_size().columns)
print(password)
print("-" * os.get_terminal_size().columns)
