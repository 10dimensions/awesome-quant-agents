import uuid
import random
from data.pricefeed import getPriceAtIndex
from utils.constants import Decisions


class Agent:
  
    def __init__(self, type, assetBalance, reserveBalance):
        self.id = uuid.uuid4()
        self.type = type
        self.assetBalance = assetBalance
        self.reserveBalance = reserveBalance

  
    def checkBalance(self, unit, quote):
        if self.assetBalance < unit:
            return Decisions.SELL_FREEZE
          
        if self.reserveBalance < quote:
            return Decisions.BUY_FREEZE

        return True

    def confirmOrder(self, decisionCheck, decision):
        if decisionCheck == Decisions.SELL_FREEZE and decision == Decisions.SELL:
            return Decisions.HOLD
        elif decisionCheck == Decisions.BUY_FREEZE and decision == Decisions.BUY:
            return Decisions.HOLD
        else:
            return decision

      
    def makeOrder(self, qty, idx):
        price = getPriceAtIndex(idx)

        decisionCheck = self.checkBalance(qty, price)
      
        decision = random.choice([ Decisions.BUY, Decisions.SELL])

        return self.confirmOrder(decisionCheck, decision)


  
    def settleOrder(self, asset, reserve):
        self.assetBalance = round(self.assetBalance + asset, 4)
        self.reserveBalance = round(self.reserveBalance + reserve, 4)
