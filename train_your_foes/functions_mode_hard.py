import numpy as np
import json

def let_computer_choose():
    l = ('bat', 'bowl') # change to a function that returns the choice based off of previous data, which means, if computer had a higher win percentage when he chose either option, go for it, random otherwise
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
    print("\t1. batsman is allowed to play one of these values \{0, 1, 2, 3, 4, 5, 6\}")
    print("\t2. each one of these values represents a the amount of runs scored on that turn")
    print("\t3. the bowler gets the same choices as the batsman, except zero")
    print("\t4. if the batsman and the bowler show the same number, the batsman is out")
    print("\t5. if the batsman is out, roles are switched")
    print("tip - if input is asked, copy paste exact string as shown by print statement")

def load_weights():
    with open("model_weights_hard.json", 'r') as w:
        weights = json.load(w)
        w_0to1 = np.array(weights["weights_0to1_hard"])
        w_1to2 = np.array(weights["weights_1to2_hard"])
        w_2to3 = np.array(weights["weights_2to3_hard"])
        w_3to4 = np.array(weights["weights_3to4_hard"])
        b_0to1 = np.array(weights["bias_0to1_hard"])
        b_1to2 = np.array(weights["bias_1to2_hard"])
        b_2to3 = np.array(weights["bias_2to3_hard"])
        b_3to4 = np.array(weights["bias_3to4_hard"])
        return w_0to1, w_1to2, w_2to3, w_3to4, b_0to1, b_1to2, b_2to3, b_3to4

def save_weights(w_0to1, w_1to2, w_2to3, w_3to4, b_0to1, b_1to2, b_2to3, b_3to4):
    weights = {
        "weights_0to1_hard" : w_0to1.tolist(),
        "weights_1to2_hard" : w_1to2.tolist(),
        "weights_2to3_hard" : w_2to3.tolist(),
        "weights_3to4_hard" : w_3to4.tolist(),
        "bias_0to1_hard" : b_0to1.tolist(),
        "bias_1to2_hard" : b_1to2.tolist(),
        "bias_2to3_hard" : b_2to3.tolist(),
        "bias_3to4_hard" : b_3to4.tolist()
    }
    with open("model_weights_hard.json", 'w') as w:
        json.dump(weights, w, indent=4)