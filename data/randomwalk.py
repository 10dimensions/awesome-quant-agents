from utils.math import arrayGenerator
from utils.math import randomUniformDistribution


class Randomwalk1D:
  
    def __init__(self, start, limit, steps):
        # Intialize Positions and Timestamp
        self.positions = [start['x']]
        self.timepoints = arrayGenerator(start['t'], start['t'] + steps, 1)  
        # 1-dimensional directions 
        self.directions = randomUniformDistribution(limit['min'], limit['max'], steps)

  
    def compute(self):
        for idx, x in enumerate(self.directions):
            # Percentage change to n-1 value (rounded-off)
            if not idx > len(self.directions)-2: 
                step = self.positions[idx] + self.positions[idx] *(x/100)
                self.positions.append(round(step,4))
      
        return { 'timepoints': self.timepoints, 'positions': self.positions }