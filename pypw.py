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
rand = ''.join([(str(i[0]+i[1])[-1:]) for i in mouse])
print()

seed = util.hashPasses(rand, 1000000, 0)
print(util.createPass(seed, 5))