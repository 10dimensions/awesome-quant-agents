import numpy as np

def arrayGenerator(start, stop, step):
    arr = np.arange(start, stop, step)
    return arr

def randomUniformDistribution(low, high, size):
    rand = np.random.uniform(low, high, size)
    return rand

def simpleMovingAverage(series, window):
    i=0
    j=0
    result = []

    while i < window - 1:
        result.append(None)
        i += 1

    #Iteration based on window size
    while j < len(series) - window + 1:
        # Average of current window
        window = round(np.sum(series[j:j+int(window)]) / window, 2)
        result.append(window)
        #Increment window right-bound
        j += 1
  
    return result
