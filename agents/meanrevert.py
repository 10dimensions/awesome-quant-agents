import data.pricefeed as PriceFeed

from agents.agent import Agent

from utils.constants import Decisions
from utils.math import percentageChange
from utils.math import liveTrailingPosition

#Inherit random agent class
class MeanRevertAgent(Agent):
    def __init__(self, type, assetBalance, reserveBalance, 
                   buyThreshold, sellThreshold, window):
        super(MeanRevertAgent, self).__init__(type, assetBalance, reserveBalance)  #Initialize base class
                     
        self.buyThreshold = buyThreshold  #Percentage Threshold for buy
        self.sellThreshold = sellThreshold  #Percentage Threshold for sell
        self.window = window  #Trailing window size


    #Compute Trailing Window Price
    def computeTrailingWindowPrice(self, idx, price):
        priceFeedInterval = PriceFeed.getPriceFeedInterval() #length of default price feed

        #Check for window boundary
        if not idx < priceFeedInterval - self.window + 1:
            return None
        
        seriesTrail = PriceFeed.getPriceFeedSlice(idx, self.window)
        return liveTrailingPosition(idx, price, seriesTrail, self.window)


    #Agent decision based on price percentage
    def getAgentDecision(self, trailingWindowPriceFeed, price, decision):
        trail_pc = percentageChange(trailingWindowPriceFeed, price)
        
        if trail_pc is None:
            return decision
          
        if trail_pc < self.buyThreshold:
            decision = Decisions.BUY
        elif trail_pc > self.sellThreshold:
            decision = Decisions.SELL

        return decision

      
    #Make order at given timepoint
    def makeOrder(self, qty, idx):
        price = PriceFeed.getPriceAtIndex(idx)  #Get price at index
        timepoint = PriceFeed.getTimepointAtIndex(idx)  #Get time point at index
        
        decision = Decisions.HOLD

        decisionCheck = self.checkBalance(qty, price)

        trailingWindowPriceFeed = self.computeTrailingWindowPrice(idx, price)
        
        if trailingWindowPriceFeed is None:
            return decision
      
        if timepoint is not None:
            decision = self.getAgentDecision(trailingWindowPriceFeed, price, decision)

        return self.confirmOrder(decisionCheck, decision)
