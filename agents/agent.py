import uuid
import random
from data.pricefeed import getPriceAtIndex
from utils.constants import Decisions


class Agent:
  
    def __init__(self, type, assetBalance, reserveBalance):
        self.id = uuid.uuid4()
        self.type = type
        self.assetBalance = assetBalance  #Initial Asset Balance
        self.reserveBalance = reserveBalance  #Initial Asset Balance

        #TODO refactor asset balance to dictionary, in order to accommodate multiple assets


    #Check if balance is sufficient to perform trade
    def checkBalance(self, unit, quote):
        if self.assetBalance < unit:
            return Decisions.SELL_FREEZE
          
        if self.reserveBalance < quote:
            return Decisions.BUY_FREEZE

        return

    #Agent decision based on price percentage
    def getAgentDecision(self):
        return random.choice([ Decisions.BUY, Decisions.SELL])

    #Prevent Order if frozen due to insufficient balance
    def confirmOrder(self, decisionCheck, decision):
        if decisionCheck == Decisions.SELL_FREEZE and decision == Decisions.SELL:
            return Decisions.HOLD
        elif decisionCheck == Decisions.BUY_FREEZE and decision == Decisions.BUY:
            return Decisions.HOLD
        else:
            return decision
          

    #Make order at given timepoint
    def makeOrder(self, qty, idx):
        price = getPriceAtIndex(idx)  #Get current price at index
        decisionCheck = self.checkBalance(qty, price)
        decision = self.getAgentDecision()  #Randomize decision

        return self.confirmOrder(decisionCheck, decision)

    
    #Modify Asset and Reserve balance after trade execution
    def settleOrder(self, asset, reserve):
        self.assetBalance = round(self.assetBalance + asset, 4)
        self.reserveBalance = round(self.reserveBalance + reserve, 4)
