from data.randomwalk import Randomwalk1D

from agents.agent import Agent
from agents.momentum import MomentumAgent

from sim.trading import TradingSim

from utils.graph import linePlots
from utils.math import simpleMovingAverage


#Sim Parameters
start = { 't': 0, 'x': 1.0 }
limit = { 'min': -1.0, 'max': +1.0 }
runs = 1000

#Final Results
dat = []


def generateData():
    print('Generating sample data...')
  
    for i in range(0,10):
        rw = Randomwalk1D(start, limit, runs)
        dat.append(rw.compute())

    print('PLOTTING...')
    linePlots(dat, 'time', 'value', '1D Random Walk Runs')

  
def simulateSimpleAgent():
    print('Simulating random agent...')
  
    priceFeed = dat[0]
    
    agent1 = Agent('random', 100, 100)
    agent2 = Agent('random', 100, 100)
    agents = [agent1, agent2]  

    sim = TradingSim(priceFeed, agents)
    result = sim.simulateAgentRun()

    print('COMPLETE...')
    #print(result)
          

def simulateMomentumAgent():
    print('Simulating Momentum Agent...')
    priceFeed = dat[0]
  
    agent1 = Agent('random', 100, 100)
    agent2 = Agent('random', 100, 100)
    agent3 = MomentumAgent('momentum', 100, 100, 2, 5, priceFeed['positions'])
    agents = [agent1, agent2, agent3]

    sim = TradingSim(priceFeed, agents)
    result = sim.simulateAgentRun()   

    print('COMPLETE...')
    #print(result)
          


if __name__ == "__main__":
    generateData()
    simulateSimpleAgent()
    simulateMomentumAgent()
    
    