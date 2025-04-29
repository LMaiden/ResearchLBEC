import numpy as np
import json
import os

def bell(x ,m ,s):
    return np.exp(-((x-m)/s)**2 /2)

def score_tracker(Array):
    return np.sum(np.abs(Array))

def Save_tojson(entity, filename, folder):
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as fp:
        json.dump(entity, fp)
        
def Load_json(filename, folder):
    filepath = os.path.join(folder, filename)
    with open(filepath, 'r') as fp:
        entity = json.load(fp)
    return entity