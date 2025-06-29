import numpy as np
import json

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

def print_rules_hard():
    print("rules:")
    print("\t1. batsman is allowed to play one of these values \{0, 1, 2, 3, 4, 5, 6\}")
    print("\t2. each one of these values represents a the amount of runs scored on that turn")
    print("\t3. the bowler gets the same choices as the batsman, except zero")
    print("\t4. if the batsman and the bowler show the same number, the batsman is out")
    print("\t5. if the batsman is out, roles are switched")
    print("tip - if input is asked, copy paste exact string as shown by print statement")
