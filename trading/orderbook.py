import enum
import queue
import time

class Order:
    def __init__(self, agent, unit, price, type):
        self.agent = agent
        self.unit = unit
        self.price = price
        self.type = type


class Trade:
    def __init(self):
    

class OrderBook:
    def __init__(self):
        self.buyOrders = []
        self.sellOrders = []

    def addOrder(self, order):
        if order.type.value is 1:
            self.buyOrders.append(order)
        elif order.type.value is 1:
            self.sellOrders.append(order)

    def processOrder(self):
        
        
  
    def clearBook(self):
        seld.orders = []
        
          