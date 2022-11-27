import data.pricefeed as PriceFeed
from agents.agent import Agent
from utils.constants import Decisions
from utils.math import runningMovingAverage

class MomentumAgent(Agent):
    def __init__(self, type, assetBalance, reserveBalance, 
                   momentumLow, momentumHigh):
        super(MomentumAgent, self).__init__(type, assetBalance, reserveBalance)
                     
        self.momentumLow = momentumLow
        self.momentumHigh = momentumHigh

  
    def makeOrder(self, qty, idx):
        decision = Decisions.HOLD

        price = PriceFeed.getPriceAtIndex(idx)
        timepoint = PriceFeed.getTimepointAtIndex(idx)

        #if j < len(self.priceFeed) - momentumLow + 1:
        seriesLow = PriceFeed.getPriceFeedSlice(idx, self.momentumLow)
        seriesHigh = PriceFeed.getPriceFeedSlice(idx, self.momentumHigh)

        avgPriceLow = runningMovingAverage(idx, seriesLow, self.momentumLow)
        avgPriceHigh = runningMovingAverage(idx, seriesHigh, self.momentumHigh)
        
        if avgPriceLow is None or avgPriceHigh is None:
            return decision
          
        if not self.checkBalance(qty, price):
            return decision
      
        if timepoint is not None:
            if avgPriceLow > avgPriceHigh:
                decision = Decisions.BUY
            else:
                decision = Decisions.SELL
        
        return decision
