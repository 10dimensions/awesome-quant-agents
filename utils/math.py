import numpy as np

def arrayGenerator(start, stop, step):
    arr = np.arange(start, stop, step)
    return arr

def randomUniformDistribution(low, high, size):
    rand = np.random.uniform(low, high, size)
    return rand
