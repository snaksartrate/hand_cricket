import numpy as np
import json
import neural_networks

def print_rules():
    print("rules:")
    print("\t1. batsman is allowed to play one of these values \{0, 1, 2, 4, 6\}")
    print("\t2. each one of these values represents a the amount of runs scored on that turn")
    print("\t3. the bowler gets the same choices as the batsman, except zero")
    print("\t4. if the batsman and the bowler show the same number, the batsman is out")
    print("\t5. if the batsman is out, roles are switched")
    print("tip - if input is asked, copy paste exact string as shown by print statement")

def let_computer_choose():
    return 'computer won', ('bat', 'bowl')[int(np.random.rand * 2)]

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

def load_weights_bats():
    with open("model_weights_medium_bats.json", 'r') as w:
        weights = json.load(w)
        w_0to1 = np.array(weights["weights_0to1_medium_bats"])
        w_1to2 = np.array(weights["weights_1to2_medium_bats"])
        w_2to3 = np.array(weights["weights_2to3_medium_bats"])
        b_0to1 = np.array(weights["bias_0to1_medium_bats"])
        b_1to2 = np.array(weights["bias_1to2_medium_bats"])
        b_2to3 = np.array(weights["bias_2to3_medium_bats"])
        return w_0to1, w_1to2, w_2to3, b_0to1, b_1to2, b_2to3

def load_weights_bowls():
    with open("model_weights_medium_bowls.json", 'r') as w:
        weights = json.load(w)
        w_0to1 = np.array(weights["weights_0to1_medium_bowls"])
        w_1to2 = np.array(weights["weights_1to2_medium_bowls"])
        w_2to3 = np.array(weights["weights_2to3_medium_bowls"])
        b_0to1 = np.array(weights["bias_0to1_medium_bowls"])
        b_1to2 = np.array(weights["bias_1to2_medium_bowls"])
        b_2to3 = np.array(weights["bias_2to3_medium_bowls"])
        return w_0to1, w_1to2, w_2to3, b_0to1, b_1to2, b_2to3

def forward_prop(ip, w0, w1, w2, b0, b1, b2, status):
    return neural_networks.compute_medium_bats(ip, w0, w1, w2, b0, b1, b2) if status == 'bats' else neural_networks.compute_medium_bowls(ip, w0, w1, w2, b0, b1, b2)


def save_weights_bats(w_0to1, w_1to2, w_2to3, b_0to1, b_1to2, b_2to3):
    weights = {
        "weights_0to1_medium_bats" : w_0to1.tolist(),
        "weights_1to2_medium_bats" : w_1to2.tolist(),
        "weights_2to3_medium_bats" : w_2to3.tolist(),
        "bias_0to1_medium_bats" : b_0to1.tolist(),
        "bias_1to2_medium_bats" : b_1to2.tolist(),
        "bias_2to3_medium_bats" : b_2to3.tolist()
    }
    with open("model_weights_medium_bats.json", 'w') as w:
        json.dump(weights, w, indent=4)

def save_weights_bowls(w_0to1, w_1to2, w_2to3, b_0to1, b_1to2, b_2to3):
    weights = {
        "weights_0to1_medium_bowls" : w_0to1.tolist(),
        "weights_1to2_medium_bowls" : w_1to2.tolist(),
        "weights_2to3_medium_bowls" : w_2to3.tolist(),
        "bias_0to1_medium_bowls" : b_0to1.tolist(),
        "bias_1to2_medium_bowls" : b_1to2.tolist(),
        "bias_2to3_medium_bowls" : b_2to3.tolist()
    }
    with open("model_weights_medium_bowls.json", 'w') as w:
        json.dump(weights, w, indent=4)