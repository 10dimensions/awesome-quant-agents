from agents.agent import Agent
from utils.constants import Decisions
from utils.math import simpleMovingAverage

class MomentumAgent(Agent):
    def __init__(self, type, assetBalance, reserveBalance, 
                   momentumLow, momentumHigh):
        super(MomentumAgent, self).__init__(type, assetBalance, reserveBalance)
                     
        self.momentumLow = momentumLow
        self.momentumHigh = momentumHigh
                     
        self.avgPriceLow = self.computeMovingAverage(momentumLow)
        self.avgPriceHigh =  self.computeMovingAverage(momentumHigh)
                     

    def checkBalance(self, unit, quote):
        if not self.assetBalance < unit or not self.reserveBalance > quote:
            return False

    def computeMovingAverage(self, val):
        return simpleMovingAverage(self.priceFeed, val)

  
    def makeOrder(self, qty, idx):
        decision = Decisions.HOLD

        price = self.priceFeed[idx]
        timepoint = self.priceFeed[idx]

        #if j < len(self.priceFeed) - momentumLow + 1:
            
        
        if self.avgPriceLow[timepoint] is None or self.avgPriceHigh[timepoint] is None:
            return decision

        if not self.checkBalance(qty, price):
            return decision
      
        if timepoint is not None:
            if self.avgPriceLow[timepoint] > self.avgPriceLow[timepoint]:
                decision = Decisions.BUY
            else:
                decision = Decisions.SELL
        
        return decision
