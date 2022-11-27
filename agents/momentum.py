import data.pricefeed as PriceFeed

from agents.agent import Agent

from utils.constants import Decisions
from utils.math import liveMovingAverage

#Inherit random agent class
class MomentumAgent(Agent):
    def __init__(self, type, assetBalance, reserveBalance, 
                   momentumLow, momentumHigh):
        super(MomentumAgent, self).__init__(type, assetBalance, reserveBalance)
                     
        self.momentumLow = momentumLow
        self.momentumHigh = momentumHigh


    #Compute Momentum Pricing
    def computeMomentumPrice(self, idx):
        priceFeedInterval = PriceFeed.getPriceFeedInterval() #length of default price feed

        #Check for window boundary
        if not idx < priceFeedInterval - self.momentumLow + 1:
            return None

        if not idx < priceFeedInterval - self.momentumHigh + 1:
            return None

        seriesLow = PriceFeed.getPriceFeedSlice(idx, self.momentumLow)
        seriesHigh = PriceFeed.getPriceFeedSlice(idx, self.momentumHigh)

        avgPriceLow = liveMovingAverage(idx, seriesLow, self.momentumLow)
        avgPriceHigh = liveMovingAverage(idx, seriesHigh, self.momentumHigh)
      
        return [avgPriceLow, avgPriceHigh]


    #Agent decision based on price momentum
    def getAgentDecision(self, momentumPrice, decision):
        if momentumPrice[0] is None or momentumPrice[1] is None:
            return decision
      

        if momentumPrice[0] > momentumPrice[1]:
            decision = Decisions.BUY
        else:
            decision = Decisions.SELL

        return decision

                     
    #Make order at given timepoint
    def makeOrder(self, qty, idx):
        price = PriceFeed.getPriceAtIndex(idx)
        timepoint = PriceFeed.getTimepointAtIndex(idx)
      
        decision = Decisions.HOLD

        decisionCheck = self.checkBalance(qty, price)
        
        momentumPrice = self.computeMomentumPrice(idx)

        if momentumPrice is None:
            return decision
      
        if timepoint is not None:
            decision = self.getAgentDecision(momentumPrice, decision)
              
        return self.confirmOrder(decisionCheck, decision)
