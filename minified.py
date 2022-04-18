import os
import sys
import hashlib
import random
import string
import subprocess
import re

args = sys.argv
length = 26
try:
    length = int(args[1])
except Exception:
    pass

platform = sys.platform

out = ""

def getMousePosition():
    out = str(subprocess.check_output(["/usr/bin/xdotool", "getmouselocation"]).decode().strip())
    print('\r', end='\r')
    regex = re.match('x:([0-9]+) y:([0-9]+) .*', out)
    return regex.group(1), regex.group(2)

def captureMouse(iterations):
    lastPos = getMousePosition()
    i = 0
    while i < iterations:
        newPos = getMousePosition()
        if newPos != lastPos:
            lastPos = newPos
            i += 1
            yield newPos[0], newPos[1]

def progressBar(i, text, maxval):
    percentage = int(100 * float(i)/float(maxval))
    iterations = int(percentage * os.get_terminal_size().columns / 100 -  len(text))
    print(text + ("-" * iterations), end='\r')

def captureRandomMouse(iterations):
    i = 0
    print("Please move your mouse", end='\r')
    for pos in captureMouse(iterations):
        i += 1
        progressBar(i, "Please move your mouse", iterations)
        yield pos

def hashPasses(hash: str, passes, index):
    hash = hash.strip().encode()
    algs = {
        'md5' : hashlib.md5,
        'sha256' : hashlib.sha256,
        'sha512' : hashlib.sha512,
    }
    
    i = 0
    for i in range(passes):
        name, hashalgo = random.choice(list(algs.items()))
        hash = hashalgo(hash).hexdigest().strip().encode()
        progressBar(i, f"Hashing pass {i}: ", passes)
        i += 1
    hash = hashlib.sha512(hash).hexdigest().strip().encode()
    print()
    
    return str(hash)

def createPass(seed, length):
    out = ""
    for i in range(length):
        seed = hashPasses(seed, 100000, i + 1)
        random.seed(seed)
        out += random.choice(string.ascii_letters + string.punctuation + string.digits)
    return out

# Generate random numbers from
# This perticular piece of code works and as long as it works you shouldnt even get close to it.
mouse = [pos for pos in captureRandomMouse(1000)]
# This is a list comprehension. Also known as the cancer of python. But it looks cool so i use it :D
rand = ''.join([(str(i[0]+i[1])[-1:]) for i in mouse])
print()

seed = hashPasses(rand, 1000000, 0)
password = createPass(seed, length)

print("-" * os.get_terminal_size().columns)
print(password)
print("-" * os.get_terminal_size().columns)