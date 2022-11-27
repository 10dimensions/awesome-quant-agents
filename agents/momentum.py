from agents.agent import Agent
from utils.constants import Decisions
from utils.math import simpleMovingAverage

class MomentumAgent(Agent):
    def __init__(self, type, assetBalance, reserveBalance, 
                   momentumLow, momentumHigh, priceFeed):
        super(MomentumAgent, self).__init__(type, assetBalance, reserveBalance, priceFeed)
                     
        self.momentumLow = momentumLow
        self.momentumHigh = momentumHigh
                     
        self.avgPriceLow = self.computeMovingAverage(momentumLow)
        self.avgPriceHigh =  self.computeMovingAverage(momentumHigh)
                     

    def checkBalance(self, reqPrice):
        if not self.assetBalance > 1 or not self.reserveBalance > 1:
            return False

    def computeMovingAverage(self, val):
        return simpleMovingAverage(self.priceFeed, val)

  
    def makeOrder(self, timepoint=None):
        decision = Decisions.HOLD
        
        if self.avgPriceLow[timepoint] is None or self.avgPriceHigh[timepoint] is None:
            return decision

        if not self.checkBalance(self.priceFeed[timepoint]):
            return decision
      
        if timepoint is not None:
            if self.avgPriceLow[timepoint] > self.avgPriceLow[timepoint]:
                decision = Decisions.BUY
            else:
                decision = Decisions.SELL
        
        return decision
