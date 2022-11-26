from agents.agent import Agent
from agents.momentum import MomentumAgent
from agents.randomwalk import Randomwalk1D

from trading.orderbook import Order
from trading.orderbook import OrderBook

from utils.graph import linePlots
from utils.math import simpleMovingAverage


#Sim Parameters
start = { 't': 0, 'x': 1.0 }
limit = { 'min': -1.0, 'max': +1.0 }

runs = 10

#Final Results
dat = []
simpleAgentTrades = []
momentumAgentTrades = []


def generateData():
    for i in range(0,10):
        rw = Randomwalk1D(start, limit, runs)
        dat.append(rw.compute())
    
    linePlots(dat, 'time', 'value', '1D Random Walk Runs')
  
  
def simulateSimpleAgent():
    priceFeed = dat[0]
    orderBook = OrderBook()
  
    agent1 = Agent('random', 100, 100)
    agent2 = Agent('random', 100, 100)
    agents = [agent1, agent2]

    result = []    

    for idx, x in enumerate(priceFeed['timepoints']):      
        for agent in agents:
            type = agent.makeOrder()
            order = Order(agent, 1, priceFeed['positions'][idx], type)
            orderBook.addOrder(order)

        orderBook.processOrder()
        orderBook.clearBook()

        r = {
          'timepoint': x,
          'price': priceFeed['positions'][idx]
        }
        
        for iag, agent in enumerate(agents):
            r['assetBalance_' + str(iag)] = agent.assetBalance
            r['reserveBalance_' + str(iag)] = agent.reserveBalance

        result.append(r)

    print(result)
          

def simulateMomentumAgent():
    priceFeed = dat[0]
    orderBook = OrderBook()
  
    agent1 = Agent('random', 100, 100)
    agent2 = Agent('random', 100, 100)
    agent3 = MomentumAgent('momentum', 100, 100, 2, 5, priceFeed['positions'])
    agents = [agent1, agent2, agent3]

    result = []    

    for idx, x in enumerate(priceFeed['timepoints']):      
        for agent in agents:
            type = agent.makeOrder(x)
            order = Order(agent, 1, priceFeed['positions'][idx], type)
            orderBook.addOrder(order)

        orderBook.processOrder()
        orderBook.clearBook()

        r = {
          'timepoint': x,
          'price': priceFeed['positions'][idx]
        }
        
        for iag, agent in enumerate(agents):
            r['assetBalance_' + str(iag)] = agent.assetBalance
            r['reserveBalance_' + str(iag)] = agent.reserveBalance

        result.append(r)

    print(result)
          


if __name__ == "__main__":
    generateData()
    #simulateSimpleAgent()
    simulateMomentumAgent()
    
    