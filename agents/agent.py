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
        if self.assetBalance < unit or self.reserveBalance < quote:
            return False

      
    def makeOrder(self, qty, idx):
        price = getPriceAtIndex(idx)
      
        if not self.checkBalance(qty, price):
            return Decisions.HOLD
      
        return random.choice([ Decisions.BUY, Decisions.SELL])

  
    def settleOrder(self, asset, reserve):
        self.assetBalance += asset
        self.reserveBalance += reserve
