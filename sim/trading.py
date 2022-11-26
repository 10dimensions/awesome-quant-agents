from trading.orderbook import Order
from trading.orderbook import OrderBook

class TradingSim:
    def __init__(self, priceFeed, agents):
        self.priceFeed = priceFeed
        self.agents = agents
        self.dat = []
        self.orderBook = OrderBook()

    def createAgentAction(self, price, timepoint=None):
        for agent in self.agents:
            type = agent.makeOrder(timepoint)
            qty = 1
            order = Order(agent, qty, price, type)
            self.orderBook.addOrder(order)

    def updateAgentBalanceSheet(self, timepoint, price):
        r = {
          'timepoint': timepoint,
          'price': price
        }
      
        for iag, agent in enumerate(self.agents):
            r['assetBalance_' + str(iag+1)] = agent.assetBalance
            r['reserveBalance_' + str(iag+1)] = agent.reserveBalance
    
        return r

    def simulateAgentRun(self):
        result = []
        for idx, x in enumerate(self.priceFeed['timepoints']):     
            self.createAgentAction(self.priceFeed['positions'][idx], x)
            self.orderBook.processOrder()
            self.orderBook.clearBook()
    
            r = self.updateAgentBalanceSheet(x, self.priceFeed['positions'][idx])
            result.append(r)
    
        return result