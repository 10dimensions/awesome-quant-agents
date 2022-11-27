import data.pricefeed as PriceFeed
from trading.orderbook import Order
from trading.orderbook import OrderBook


class TradingSim:
  
    def __init__(self, agents):
        self.agents = agents
        self.dat = []
        self.orderBook = OrderBook()

  
    def createAgentAction(self, qty, idx, timepoint=None):
        for agent in self.agents:
            price = PriceFeed.getPriceAtIndex(idx)
            type = agent.makeOrder(qty, idx)
            order = Order(agent, qty, price, type)
            self.orderBook.addOrder(order)

  
    def updateAgentBalanceSheet(self, idx):
        r = {
          'timepoint': PriceFeed.getTimepointAtIndex(idx),
          'price': PriceFeed.getPriceAtIndex(idx)
        }
      
        for iag, agent in enumerate(self.agents):
            r['assetBalance_' + str(iag+1)] = agent.assetBalance
            r['reserveBalance_' + str(iag+1)] = agent.reserveBalance
    
        return r

  
    def simulateAgentRun(self):
        result = []
        duration = PriceFeed.getPriceFeedInterval()
        for idx in range(duration): 
            qty = 1
            self.createAgentAction(qty, idx)
            self.orderBook.processOrder()
            self.orderBook.clearBook()
    
            r = self.updateAgentBalanceSheet(idx)
            result.append(r)
    
        return result