import data.pricefeed as PriceFeed

from agents.agent import Agent
from agents.meanrevert import MeanRevertAgent
from agents.momentum import MomentumAgent

from sim.trading import TradingSim

from utils.graph import linePlots
from utils.io import saveResult


# Generate Sample Data
def generateData():
    print('Generating sample data...')
    PriceFeed.createPriceFeed()
    
    print('PLOTTING...')
    linePlots(PriceFeed.data, 'time', 'value', '1D Random Walk Runs')


# Simulate Simple Agent with Random decision-making
def simulateSimpleAgent():
    print('Simulating random agent...')

    #Iteration of PriceFeed (Default to first iteration)
    PriceFeed.setSimIteration(5)
    
    agent1 = Agent('random', 100, 100)  #Initialize (name, assets, reserve)
    agent2 = Agent('random', 100, 100)  #Initialize (name, assets, reserve)
    agents = [agent1, agent2]  

    # Initialize and run simulation
    sim = TradingSim(agents)
    result = sim.simulateAgentRun()

    print('COMPLETE...')
    saveResult(result, 'random.json')
          

def simulateMomentumAgent():
    print('Simulating Momentum Agent...')

    #Iteration of PriceFeed (Default to first iteration)
    PriceFeed.setSimIteration(5)
  
    agent1 = Agent('random', 100, 100)  #Initialize (name, asset, reserve)
    agent2 = Agent('random', 100, 100)  #Initialize (name, asset, reserve)
    agent3 = MomentumAgent('momentum', 100, 100, 2, 5)  #Initialize (name, asset, reserve, ma_win_low, ma_win_high)
    agents = [agent1, agent2, agent3]

    # Initialize and run simulation
    sim = TradingSim(agents)
    result = sim.simulateAgentRun()   

    print('COMPLETE...')
    saveResult(result, 'momentum.json')
    #print(result)

def simulateMeanRevertAgent():
    print('Simulating Mean Revert Agent...')

    #Iteration of PriceFeed (Default to first iteration)
    PriceFeed.setSimIteration(5)
  
    agent1 = Agent('random', 100, 100)  #Initialize (name, asset, reserve)
    agent2 = Agent('random', 100, 100)  #Initialize (name, asset, reserve)
    agent3 = MomentumAgent('momentum', 100, 100, 2, 5)  #Initialize (name, asset, reserve, ma_win_low, ma_win_high)
    agent4 = MeanRevertAgent('meanrevert', 100, 100, 25, 75, 4)  #Initialize (name, asset, reserve, buy_pc, sell_pc, window)
    agents = [agent1, agent2, agent3, agent4]

    # Initialize and run simulation
    sim = TradingSim(agents)
    result = sim.simulateAgentRun()   

    print('COMPLETE...')
    saveResult(result, 'meanrevert.json')
          

if __name__ == "__main__":
    generateData()
    simulateSimpleAgent()
    simulateMomentumAgent()
    simulateMeanRevertAgent()
    
    