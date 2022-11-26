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
        '''
        # Average of current window
        avg = arr[i : i + window_size]
        window = round(sum(series[j:j+int(window)]) / window, 4)
        result.append(window)
        #Increment window right-bound
        j += 1
        '''
        
        # Store elements from i to i+window_size
        # in list to get the current window
        slice = series[j : j + int(window)]
      
        # Calculate the average of current window
        window_average = round(sum(slice) / window, 4)
          
        # Store the average of current
        # window in moving average list
        result.append(window_average)
          
        # Shift window to right by one position
        j += 1
  
    return result
