import numpy as np
import json

def leaky_relu(x):
    return np.where(x >= 0, x, 0.01 * x)

def softmax(x):
    exps = np.exp(x - np.max(x))
    return exps / np.sum(exps)

def compute_easy(ip, w0, w1, w2, b0, b1, b2):
    l1 = leaky_relu(ip @ w0 + b0)
    l2 = leaky_relu(l1 @ w1 + b1)
    op = softmax(l2 @ w2 + b2)
    return (1, 2, 4, 6)[np.argmax(op)]

def compute_medium(ip, w0, w1, w2, b0, b1, b2):
    l1 = leaky_relu(ip @ w0 + b0)
    l2 = leaky_relu(l1 @ w1 + b1)
    op = softmax(l2 @ w2 + b2)
    return (0, 1, 2, 4, 6)[np.argmax(op)]

def compute_hard_bats_first_inning(ip, w0, w1, w2, w3, b0, b1, b2, b3):
    pass

def compute_hard_bats_second_inning(ip, w0, w1, w2, w3, b0, b1, b2, b3):
    pass

def compute_hard_bowls_first_inning(ip, w0, w1, w2, w3, b0, b1, b2, b3):
    pass

def compute_hard_bowls_second_inning(ip, w0, w1, w2, w3, b0, b1, b2, b3):
    pass