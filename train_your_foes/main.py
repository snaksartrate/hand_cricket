import numpy as np
import json

no_of_overs = 0
while no_of_overs not in (2, 5, 10, 15, 20):
    no_of_overs = int(input("choose the total number of overs:\n2\t5\t10\t15\t20\n"))

mode = 'a'
while mode not in ('e', 'm', 'h'):
    mode = input("choose mode\ne\tm\th\n")
