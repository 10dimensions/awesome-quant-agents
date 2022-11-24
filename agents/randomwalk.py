from utils.math import arrayGenerator
from utils.math import randomUniformDistribution

def randomwalk1D(start, limit, steps):
    # Intialize Positions and Timestamp
    positions = [start['x']]
    timepoints = arrayGenerator(start['t'], start['t'] + steps, 1)  

    # 1-dimensional directions 
    directions = randomUniformDistribution(limit['min'], limit['max'], steps)
  
    for idx, x in enumerate(directions):
        # Percentage change to n-1 value
        if not idx > len(directions)-2: 
            step = positions[idx] + positions[idx] * (x/100)
            positions.append(step)
      
    return timepoints, positions