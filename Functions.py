import numpy as np

def bell(x ,m ,s):
    return np.exp(-((x-m)/s)**2 /2)

def score_tracker(Array):
    return np.sum(np.abs(Array))

