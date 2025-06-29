import numpy as np
import subprocess
import sys

no_of_overs = 0
while no_of_overs not in (2, 5, 10, 15, 20):
    no_of_overs = int(input("choose the total number of overs:\n2\t5\t10\t15\t20\n"))

mode = 'a'
while mode not in ('e', 'm', 'h'):
    mode = input("choose mode\ne\tm\th\n")

if mode == 'e':
    print("easy mode")
    subprocess.run([sys.executable, "easy.py", no_of_overs])
elif mode == 'm':
    print("medium mode")
    subprocess.run([sys.executable, "medium.py", no_of_overs])
else:
    print("hard mode")
    subprocess.run([sys.executable, "hard.py", no_of_overs])