from utils.constants import Decisions
import uuid
import random

class Agent:
  
    def __init__(self, type, assetBalance, reserveBalance, priceFeed):
        self.id = uuid.uuid4()
        self.type = type
        self.assetBalance = assetBalance
        self.reserveBalance = reserveBalance
        self.priceFeed = priceFeed

  
    def checkBalance(self, reqPrice):
        if not self.assetBalance > 0 or not self.reserveBalance > reqPrice:
            return False

      
    def makeOrder(self, price, timepoint=None):
        decisions = [ Decisions.BUY, Decisions.SELL]

        decision = random.choice(decisions)
        return decision

  
    def settleOrder(self, asset, reserve):
        self.assetBalance += asset
        self.reserveBalance += reserve
