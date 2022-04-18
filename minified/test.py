import os
import time

def progressBar(i, text, maxval):
    percentage = int(100 * float(i)/float(maxval))
    iterations = int(percentage * os.get_terminal_size().columns / 100 -  len(text))
    print(text + ("-" * iterations), end='\r')


for i in range(100):
    progressBar(i, "testing", 100)
    time.sleep(0.1)

print()