import data.pricefeed as PriceFeed
from trading.orderbook import Order
from trading.orderbook import OrderBook


class TradingSim:
  
    def __init__(self, agents):
        self.agents = agents  #Initialize patifcipating agents
        self.dat = []
        self.orderBook = OrderBook()  #Initialize new order book


    #Perform Agent Action
    def createAgentAction(self, qty, idx, timepoint=None):
        for agent in self.agents:
            price = PriceFeed.getPriceAtIndex(idx)
            type = agent.makeOrder(qty, idx)
            order = Order(agent, qty, price, type)
            self.orderBook.addOrder(order)


    #Update balancesheet of agents
    def updateAgentBalanceSheet(self, idx):
        r = {
          'timepoint': PriceFeed.getTimepointAtIndex(idx),
          'price': PriceFeed.getPriceAtIndex(idx)
        }

        #Append balance to each price, time record of all agents
        for iag, agent in enumerate(self.agents):
            r['assetBalance_' + str(iag+1)] = agent.assetBalance
            r['reserveBalance_' + str(iag+1)] = agent.reserveBalance
    
        return r


    #Start simulation run with initialized agents
    def simulateAgentRun(self):
        result = []
        duration = PriceFeed.getPriceFeedInterval()  #Get total interval
        for idx in range(duration): 
            qty = 1  #Default Qty of 1, extensible
            self.createAgentAction(qty, idx)
            self.orderBook.processOrder()  #Process all orders from agents 
            self.orderBook.clearBook()  #Clear Orderbook at each timestamp
    
            r = self.updateAgentBalanceSheet(idx)
            result.append(r)
    
        return result