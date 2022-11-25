from utils.constans import Decisions
import uuid

class SimpleAgent:
  
    def __init__(self, type, assetBalance, reserveBalance):
        self.id = uuid.uuid4()
        self.type = type
        self.assetBalance = assetBalance
        self.reserveBalance = reserveBalance

      
    def makeOrder(self, price):
        decision = random.choice(list(Decisions))
        return decision

  
    def settleOrder(self, asset, reserve):
        self.assetBalance += assetBalance
        self.reserve += reserve