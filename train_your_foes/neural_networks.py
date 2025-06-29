import numpy as np
import json

def leaky_relu(x):
    return np.where(x >= 0, x, 0.01 * x)

def leaky_relu_derivative(x):
    return np.where(x >= 0, 1, 0.01)

def softmax(x):
    exps = np.exp(x - np.max(x))
    return exps / np.sum(exps)

def compute_easy_bats(ip, w0, w1, w2, b0, b1, b2):
    z0 = ip @ w0 + b0
    l1 = leaky_relu(z0)
    z1 = l1 @ w1 + b1
    l2 = leaky_relu(z1)
    z2 = l2 @ w2 + b2
    op = softmax(z2)
    return (1, 2, 4, 6)[np.argmax(op)]

def compute_easy_bowls(ip, w0, w1, w2, b0, b1, b2):
    z0 = ip @ w0 + b0
    l1 = leaky_relu(z0)
    z1 = l1 @ w1 + b1
    l2 = leaky_relu(z1)
    z2 = l2 @ w2 + b2
    op = softmax(z2)
    return (1, 2, 4, 6)[np.argmax(op)]

def compute_medium_bats(ip, w0, w1, w2, b0, b1, b2):
    z0 = ip @ w0 + b0
    l1 = leaky_relu(z0)
    z1 = l1 @ w1 + b1
    l2 = leaky_relu(z1)
    z2 = l2 @ w2 + b2
    op = softmax(z2)
    return (0, 1, 2, 4, 6)[np.argmax(op)]

def compute_medium_bowls(ip, w0, w1, w2, b0, b1, b2):
    z0 = ip @ w0 + b0
    l1 = leaky_relu(z0)
    z1 = l1 @ w1 + b1
    l2 = leaky_relu(z1)
    z2 = l2 @ w2 + b2
    op = softmax(z2)
    return (0, 1, 2, 4, 6)[np.argmax(op)]

def compute_hard_bats_first_inning(ip, w0, w1, w2, w3, b0, b1, b2, b3):
    z0 = ip @ w0 + b0
    l1 = leaky_relu(z0)
    z1 = l1 @ w1 + b1
    l2 = leaky_relu(z1)
    z2 = l2 @ w2 + b2
    l3 = leaky_relu(z2)
    z3 = l3 @ w3 + b3
    op = softmax(z3)
    return (0, 1, 2, 4, 6)[np.argmax(op)]

def compute_hard_bats_second_inning(ip, w0, w1, w2, w3, b0, b1, b2, b3):
    z0 = ip @ w0 + b0
    l1 = leaky_relu(z0)
    z1 = l1 @ w1 + b1
    l2 = leaky_relu(z1)
    z2 = l2 @ w2 + b2
    l3 = leaky_relu(z2)
    z3 = l3 @ w3 + b3
    op = softmax(z3)
    return (0, 1, 2, 4, 6)[np.argmax(op)]

def compute_hard_bowls_first_inning(ip, w0, w1, w2, w3, b0, b1, b2, b3):
    z0 = ip @ w0 + b0
    l1 = leaky_relu(z0)
    z1 = l1 @ w1 + b1
    l2 = leaky_relu(z1)
    z2 = l2 @ w2 + b2
    l3 = leaky_relu(z2)
    z3 = l3 @ w3 + b3
    op = softmax(z3)
    return (0, 1, 2, 4, 6)[np.argmax(op)]

def compute_hard_bowls_second_inning(ip, w0, w1, w2, w3, b0, b1, b2, b3):
    z0 = ip @ w0 + b0
    l1 = leaky_relu(z0)
    z1 = l1 @ w1 + b1
    l2 = leaky_relu(z1)
    z2 = l2 @ w2 + b2
    l3 = leaky_relu(z2)
    z3 = l3 @ w3 + b3
    op = softmax(z3)
    return (0, 1, 2, 4, 6)[np.argmax(op)]

