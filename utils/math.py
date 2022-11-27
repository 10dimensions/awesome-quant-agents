import numpy as np

def percentageChange(current,previous):
    if current and previous !=0:
        return round((current/previous)-1*100,2)
    else:
        return None

def arrayGenerator(start, stop, step):
    arr = np.arange(start, stop, step)
    return arr

def randomUniformDistribution(low, high, size):
    rand = np.random.uniform(low, high, size)
    return rand


def runningMovingAverage(currentTimePoint, series, window):
    i=0
    result = None

    if currentTimePoint < window -1:
        return result

    #Iteration based on window size
    if j < len(series) - window + 1:        
        # Store elements in current window
        slice = series[j : j + int(window)]
      
        # Average of current window
        window_average = round(sum(slice) / window, 4)
        result = window_average
  
    return result


def simpleMovingAverage(series, window):
    i=0
    j=0
    result = []

    while i < window - 1:
        result.append(None)
        i += 1

    #Iteration based on window size
    while j < len(series) - window + 1:        
        # Store elements in current window
        slice = series[j : j + int(window)]
      
        # Average of current window
        window_average = round(sum(slice) / window, 4)
        result.append(window_average)
          
        j += 1
  
    return result


def trailingWindowPosition(series, window):
    i=0
    j=0
    result = []

    while i < window - 1:
        result.append(None)
        i += 1

    #Iteration based on window size
    while j < len(series) - window + 1:        
        # Store elements in current window
        slice = series[j : j + int(window)]
      
        # Trailing Position Compute
        trailing_price = round(series[j] - min(slice), 4)
        range = round(max(slice) - min(slice), 4)
        window_trailing_position = trailing_price / range
        result.append(window_trailing_position)
          
        j += 1
  
    return result

