import numpy as np
import json

def let_computer_choose():
    l = ('bat', 'bowl')
    return 'computer won', l[int(np.random.rand * 2)]

def toss():
    h = input("enter h/t: ")
    if h != 'h' and h != 't':
        return let_computer_choose()
    if np.random.rand >= 0.5:
        print("human won")
        human_chooses_to = 'run lol'
        while human_chooses_to not in ('bat', 'bowl'):
            human_chooses_to = input("human chooses to: ")
        return 'human won', human_chooses_to
    else:
        return let_computer_choose()

def print_rules():
    print("rules:")
    print("\t1. batsman is allowed to play one of these values \{1, 2, 4, 6\}")
    print("\t2. each one of these values represents a the amount of runs scored on that turn")
    print("\t3. the bowler gets the same choices as the batsman")
    print("\t4. if the batsman and the bowler show the same number, the batsman is out")
    print("\t5. if the batsman is out, roles are switched")
    print("tip - if input is asked, copy paste exact string as shown by print statement")

def load_weights():
    pass

def save_weights():
    pass