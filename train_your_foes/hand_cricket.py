import numpy as np
import json
import easy_mode
import medium_mode
import hard_mode

no_of_overs = 0
while no_of_overs not in (2, 5, 10, 15, 20):
    no_of_overs = int(input("choose the total number of overs:\n2\t5\t10\t15\t20\n"))

mode = 'a'
while mode not in ('e', 'm', 'h'):
    mode = input("choose mode\ne\tm\th\n")

def print_rules_hard():
    print("rules:")
    print("\t1. batsman is allowed to play one of these values \{0, 1, 2, 3, 4, 5, 6\}")
    print("\t2. each one of these values represents a the amount of runs scored on that turn")
    print("\t3. the bowler gets the same choices as the batsman, except zero")
    print("\t4. if the batsman and the bowler show the same number, the batsman is out")
    print("\t5. if the batsman is out, roles are switched")
    print("tip - if input is asked, copy paste exact string as shown by print statement")

def inning_complete():
    # if both threw the same number
    pass
