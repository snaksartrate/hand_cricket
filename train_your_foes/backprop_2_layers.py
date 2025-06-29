import numpy as np

def dz2(a2, y):
    return a2 - y

def dw2(a2, y, a1):
    return dz2(a2, y) @ a1

def w2_new(y, w2, a2, a1, alpha):
    return w2 - alpha * dw2(a2, y, a1)
# w2 = w2_new(y, w2, a2, a1, alpha) is what will be written