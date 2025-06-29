import numpy as np
import json

def LeakyReLU(x):
    return np.where(x >= 0, x, 0.01 * x)

def softmax(x):
    exps = np.exp(x - np.max(x))
    return exps / np.sum(exps)

def compute_easy_bats():
    pass

def compute_easy_bowls():
    pass

def compute_medium_bats():
    pass

def compute_medium_bowls():
    pass

def compute_hard_bats_first_inning():
    pass

def compute_hard_bats_second_inning():
    pass

def compute_hard_bowls_first_inning():
    pass

def compute_hard_bowls_second_inning():
    pass