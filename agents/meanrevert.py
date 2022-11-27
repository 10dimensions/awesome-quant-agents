import data.pricefeed as PriceFeed
from agents.agent import Agent
from utils.constants import Decisions
from utils.math import percentageChange
from utils.math import liveTrailingPosition

class MeanRevertAgent(Agent):
    def __init__(self, type, assetBalance, reserveBalance, 
                   buyThreshold, sellThreshold, window):
        super(MeanRevertAgent, self).__init__(type, assetBalance, reserveBalance)
                     
        self.buyThreshold = buyThreshold
        self.sellThreshold = sellThreshold
        self.window = window


    def computeTrailingPricePosition(self):
        return trailingWindowPosition(self.priceFeed, self.window)
  
  
    def makeOrder(self, qty, idx):
        price = PriceFeed.getPriceAtIndex(idx)
        timepoint = PriceFeed.getTimepointAtIndex(idx)
        priceFeedInterval = PriceFeed.getPriceFeedInterval()
        decision = Decisions.HOLD

        if not self.checkBalance(qty, price):
            return decision

        if not idx < priceFeedInterval - self.window + 1:
            return decision

        seriesTrail = PriceFeed.getPriceFeedSlice(idx, self.window)
        trailingWindowPriceFeed = liveTrailingPosition(idx, price, seriesTrail, self.window)
        
        if trailingWindowPriceFeed is None:
            return decision
      
        if timepoint is not None:
            trail_pc = percentageChange(trailingWindowPriceFeed, price)
            if trail_pc is None:
                return decision
              
            if trail_pc < self.buyThreshold:
                decision = Decisions.BUY
            elif trail_pc > self.sellThreshold:
                decision = Decisions.SELL

        print(trail_pc)
        print(decision)
        return decision
