import pyautogui
import hashlib
import progressbar
import random
import string

def captureMouse(iterations):
    lastPos = pyautogui.position()
    i = 0
    while i < iterations:
        newPos = pyautogui.position()
        if newPos != lastPos:
            lastPos = newPos
            i += 1
            yield newPos.x, newPos.y

def captureRandomMouse(iterations):
    i = 0
    widgets = ["Please move your mouse :", progressbar.Bar()]
    bar = progressbar.ProgressBar(widgets=widgets, maxval=iterations).start()
    for pos in captureMouse(iterations):
        i += 1
        bar.update(i)
        yield pos

def hashPasses(hash: str, passes, index):
    hash = hash.strip().encode()
    algs = {
        'md5' : hashlib.md5,
        'sha256' : hashlib.sha256,
        'sha512' : hashlib.sha512,
    }
    
    i = 0
    widgets = [f"Hashing pass {index} please wait:", progressbar.Bar(), progressbar.AdaptiveETA()]
    bar = progressbar.ProgressBar(widgets=widgets, maxval=passes).start()
    for i in range(passes):
        name, hashalgo = random.choice(list(algs.items()))
        hash = hashalgo(hash).hexdigest().strip().encode()
        bar.update(i)
        i += 1
    hash = hashlib.sha512(hash).hexdigest().strip().encode()
    print()
    
    return str(hash)

def createPass(seed, length):
    out = ""
    for i in range(length):
        seed = hashPasses(seed, 1000000, i + 1)
        random.seed(seed)
        out += random.choice(string.ascii_letters + string.punctuation + string.digits)
    return out