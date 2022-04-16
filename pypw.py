#!/usr/bin/env python

# Secure password generator written in python.

import threading
import sys
import util

platform = sys.platform

length = 32

out = ""

# Generate random numbers from
# Do NOT TOUCH THIS CODE! It works, and as long as it works you shouldnt even get close to it.
mouse = [pos for pos in util.captureRandomMouse(1000)]
seed = ''.join([(str(i[0]+i[1])[-1:]) for i in mouse])
print()

print(util.hashPasses(seed, 10000000))