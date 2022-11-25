from utils.constants import Decisions
import uuid
import random

class Agent:
  
    def __init__(self, type, assetBalance, reserveBalance):
        self.id = uuid.uuid4()
        self.type = type
        self.assetBalance = assetBalance
        self.reserveBalance = reserveBalance

      
    def makeOrder(self, price=None):
        decision = random.choice(list(Decisions))
        return decision

  
    def settleOrder(self, asset, reserve):
        self.assetBalance += asset
        self.reserveBalance += reserve
