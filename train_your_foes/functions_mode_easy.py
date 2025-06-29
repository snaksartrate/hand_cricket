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
    with open("model_weights_easy.json", 'r') as w:
        weights = json.load(w)
        w_0to1 = np.array(weights["weights_0to1_easy"])
        w_1to2 = np.array(weights["weights_1to2_easy"])
        b_0to1 = np.array(weights["bias_0to1_easy"])
        b_1to2 = np.array(weights["bias_1to2_easy"])
        return w_0to1, w_1to2, b_0to1, b_1to2

def save_weights(w_0to1, w_1to2, b_0to1, b_1to2):
    weights = {
        "weights_0to1_easy" : w_0to1.tolist(),
        "weights_1to2_easy" : w_1to2.tolist(),
        "bias_0to1_easy" : b_0to1.tolist(),
        "bias_1to2_easy" : b_1to2.tolist()
    }
    with open("model_weights_easy.json", 'w') as w:
        json.dump(weights, w, indent=4)