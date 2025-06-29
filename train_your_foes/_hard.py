import numpy as np
import json
import sys

no_of_overs = int(sys.argv[1])

def let_computer_choose_hard():
    l = ('bat', 'bowl') # change to a function that returns the choice based off of previous data, which means, if computer had a higher win percentage when he chose either option, go for it, random otherwise
    return 'computer won', l[int(np.random.rand * 2)]

def toss_hard():
    h = input("enter h/t: ")
    if h != 'h' and h != 't':
        return let_computer_choose_hard()
    if np.random.rand >= 0.5:
        print("human won")
        human_chooses_to = 'run lol'
        while human_chooses_to not in ('bat', 'bowl'):
            human_chooses_to = input("human chooses to: ")
        return 'human won', human_chooses_to
    else:
        return let_computer_choose_hard()

