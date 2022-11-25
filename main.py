from agents.randomwalk import Randomwalk1D
from utils.graph import linePlots
from utils.math import simpleMovingAverage

#Sim Parameters
start = { 't': 0, 'x': 1.0 }
limit = { 'min': -1.0, 'max': +1.0 }

runs = 1000

#Final Results
dat = []


def generateData():
    for i in range(0,10):
        rw = Randomwalk1D(start, limit, runs)
        dat.append(rw.compute())
    
    linePlots(dat, 'time', 'value', '1D Random Walk Runs')
  
  
def simulateSimpleAgent():
    simpleMovingAverage([1, 2, 3, 7, 9], 3)
    

if __name__ == "__main__":
    generateData()
    
    print(dat[0])
    