import enum
import queue
import random
import time


class Order:
    def __init__(self, agent, unit, price, type):
        self.agent = agent
        self.unit = unit
        self.price = price
        self.type = type


class Trades:
    def __init__(self):
        self.history = []

    #Append trade object
    def updateTrades(self, buyerID, sellerID, unit, price):
        self.history.append({
          'buyerID' : buyerID,
          'sellerID' : sellerID,
          'unit' : unit,
          'price' : price
        })
    

class OrderBook:
    def __init__(self):
        self.buyOrders = []
        self.sellOrders = []
        self.trades = Trades()

    #Update orderbook
    def addOrder(self, order):
        if order.type.value == 1:
            self.buyOrders.append(order)
        elif order.type.value == 2:
            self.sellOrders.append(order)


    def clearBook(self):
      
        # TODO
        # Refund uncleared Orders
      
        self.buyOrders = []
        self.sellOrders = []
      

    def processOrder(self):
      
        # TODO
        # Atomic Balance Deductions
      
        while len(self.buyOrders) > 0 and len(self.sellOrders) > 0:
            #Random choice of sell order
            rn1 = random.randint(0,len(self.sellOrders)-1)
            sellerAgent = self.sellOrders[rn1].agent

            #Random choice of buy order
            rn2 = random.randint(0,len(self.buyOrders)-1)
            buyerAgent = self.buyOrders[rn2].agent
            
            unit = self.sellOrders[rn1].unit
            price = self.sellOrders[rn1].price

            #Settle Order after successful trade
            buyerAgent.settleOrder(unit, -price)
            sellerAgent.settleOrder(-unit, price)

            #Update trade history
            self.trades.updateTrades(buyerAgent.id, sellerAgent.id, unit, price)

            #Remove processed orders
            self.sellOrders.pop(rn1)
            self.buyOrders.pop(rn2)

        