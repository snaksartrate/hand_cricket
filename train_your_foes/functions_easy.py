import numpy as np
import json
import neural_networks
import backprop_2_layers

def print_rules():
    print("rules:")
    print("\t1. batsman is allowed to play one of these values \{1, 2, 4, 6\}")
    print("\t2. each one of these values represents a the amount of runs scored on that turn")
    print("\t3. the bowler gets the same choices as the batsman")
    print("\t4. if the batsman and the bowler show the same number, the batsman is out")
    print("\t5. if the batsman is out, roles are switched")
    print("tip - if input is asked, copy paste exact string as shown by print statement")

def let_computer_choose():
    return 'computer won', 'bat' # consider in easy mode, computer bats first

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
    with open("model_weights_easy_bats.json", 'r') as w:
        weights = json.load(w)
        w_0to1 = np.array(weights["weights_0to1_easy_bats"])
        w_1to2 = np.array(weights["weights_1to2_easy_bats"])
        w_2to3 = np.array(weights["weights_2to3_easy_bats"])
        b_0to1 = np.array(weights["bias_0to1_easy_bats"])
        b_1to2 = np.array(weights["bias_1to2_easy_bats"])
        b_2to3 = np.array(weights["bias_2to3_easy_bats"])
        return w_0to1, w_1to2, w_2to3, b_0to1, b_1to2, b_2to3

def load_weights_bowls():
    with open("model_weights_easy_bowls.json", 'r') as w:
        weights = json.load(w)
        w_0to1 = np.array(weights["weights_0to1_easy_bowls"])
        w_1to2 = np.array(weights["weights_1to2_easy_bowls"])
        w_2to3 = np.array(weights["weights_2to3_easy_bowls"])
        b_0to1 = np.array(weights["bias_0to1_easy_bowls"])
        b_1to2 = np.array(weights["bias_1to2_easy_bowls"])
        b_2to3 = np.array(weights["bias_2to3_easy_bowls"])
        return w_0to1, w_1to2, w_2to3, b_0to1, b_1to2, b_2to3

def episodes():
    pass

def forward_prop(ip, w0, w1, w2, b0, b1, b2, status):
    return neural_networks.compute_easy_bats(ip, w0, w1, w2, b0, b1, b2) if status == 'bats' else neural_networks.compute_easy_bowls(ip, w0, w1, w2, b0, b1, b2)

def back_prop_bats(y, w2, w1, w0, a2, a1, a0, alpha):
    w2 = backprop_2_layers.w2_new(y, w2, a2, a1, alpha)
    
    pass

def back_prop_bowls():
    pass

def save_weights_bats(w_0to1, w_1to2, w_2to3, b_0to1, b_1to2, b_2to3):
    weights = {
        "weights_0to1_easy_bats" : w_0to1.tolist(),
        "weights_1to2_easy_bats" : w_1to2.tolist(),
        "weights_2to3_easy_bats" : w_2to3.tolist(),
        "bias_0to1_easy_bats" : b_0to1.tolist(),
        "bias_1to2_easy_bats" : b_1to2.tolist(),
        "bias_2to3_easy_bats" : b_2to3.tolist()
    }
    with open("model_weights_easy_bats.json", 'w') as w:
        json.dump(weights, w, indent=4)

def save_weights_bowls(w_0to1, w_1to2, w_2to3, b_0to1, b_1to2, b_2to3):
    weights = {
        "weights_0to1_easy_bowls" : w_0to1.tolist(),
        "weights_1to2_easy_bowls" : w_1to2.tolist(),
        "weights_2to3_easy_bowls" : w_2to3.tolist(),
        "bias_0to1_easy_bowls" : b_0to1.tolist(),
        "bias_1to2_easy_bowls" : b_1to2.tolist(),
        "bias_2to3_easy_bowls" : b_2to3.tolist()
    }
    with open("model_weights_easy_bowls.json", 'w') as w:
        json.dump(weights, w, indent=4)