from agents.agent import Agent
from utils.constants import Decisions
from utils.math import simpleMovingAverage
from utils.math import percentageChange
from utils.math import trailingWindowPosition

class MeanRevertAgent(Agent):
    def __init__(self, type, assetBalance, reserveBalance, 
                   buyThreshold, sellThreshold, window, priceFeed):
        super(MeanRevertAgent, self).__init__(type, assetBalance, reserveBalance, priceFeed)
                     
        self.buyThreshold = buyThreshold
        self.sellThreshold = sellThreshold
        self.window = window
                    
        self.trailingWindowPriceFeed = self.computeTrailingPricePosition()


    def computeTrailingPricePosition(self):
        return trailingWindowPosition(self.priceFeed, self.window)
  
  
    def makeOrder(self, timepoint=None):
        decision = Decisions.HOLD
        
        if self.trailingWindowPriceFeed[timepoint] is None:
            return decision
      
        if timepoint is not None:
            trail_pc = percentageChange(self.trailingWindowPriceFeed[timepoint], self.priceFeed[timepoint])
            if trail_pc is None:
                return decision
              
            if trail_pc <= -self.buyThreshold:
                decision = Decisions.BUY
            elif trail_pc >= self.sellThreshold:
                decision = Decisions.SELL
        
        return decision
