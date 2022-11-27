import data.pricefeed as PriceFeed

from agents.agent import Agent
from agents.meanrevert import MeanRevertAgent
from agents.momentum import MomentumAgent

from sim.trading import TradingSim

from utils.graph import linePlots
from utils.io import saveResult


def generateData():
    print('Generating sample data...')
    PriceFeed.createPriceFeed()
    
    print('PLOTTING...')
    linePlots(PriceFeed.data, 'time', 'value', '1D Random Walk Runs')

  
def simulateSimpleAgent():
    print('Simulating random agent...')

    #Iteration of PriceFeed (Default to first iteration)
    PriceFeed.setSimIteration(5)
    
    agent1 = Agent('random', 100, 100)
    agent2 = Agent('random', 100, 100)
    agents = [agent1, agent2]  

    sim = TradingSim(agents)
    result = sim.simulateAgentRun()

    print('COMPLETE...')
    saveResult(result, 'random.json')
    #print(result)
          

def simulateMomentumAgent():
    print('Simulating Momentum Agent...')

    #Iteration of PriceFeed (Default to first iteration)
    PriceFeed.setSimIteration(5)
  
    agent1 = Agent('random', 100, 100)
    agent2 = Agent('random', 100, 100)
    agent3 = MomentumAgent('momentum', 100, 100, 2, 5)
    agents = [agent1, agent2, agent3]

    sim = TradingSim(agents)
    result = sim.simulateAgentRun()   

    print('COMPLETE...')
    saveResult(result, 'momentum.json')
    #print(result)

def simulateMeanRevertAgent():
    print('Simulating Mean Revert Agent...')

    #Iteration of PriceFeed (Default to first iteration)
    PriceFeed.setSimIteration(5)
  
    agent1 = Agent('random', 100, 100)
    agent2 = Agent('random', 100, 100)
    agent3 = MomentumAgent('momentum', 100, 100, 2, 5)
    agent4 = MeanRevertAgent('meanrevert', 100, 100, 25, 75, 4)
    agents = [agent1, agent2, agent3, agent4]

    sim = TradingSim(agents)
    result = sim.simulateAgentRun()   

    print('COMPLETE...')
    saveResult(result, 'meanrevert.json')
    #print(result)
          

if __name__ == "__main__":
    generateData()
    simulateSimpleAgent()
    simulateMomentumAgent()
    simulateMeanRevertAgent()
    
    