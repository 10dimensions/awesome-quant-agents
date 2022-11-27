from utils.math import randomWalk1D
from utils.graph import linePlots


#Sim Parameters
start = { 't': 0, 'x': 1.0 }  #Start params
limit = { 'min': -1.0, 'max': +1.0 }  #Price change limit
runs = 1000
totalIterations = 10
simIteration = 0

#Data store
data = []
datHash = None #TODO pricefeed dictionary


#Create random pricefeed
def createPriceFeed():
    for i in range(0,totalIterations):
        rw = randomWalk1D(start, limit, runs)
        data.append(rw)


def getPriceAtIndex(idx):
    return data[simIteration]["positions"][idx]


#def getPriceAtTimepoint():
#    return

def getPriceFeedInterval():
    return len(data[simIteration]['timepoints'])


def getPriceFeedSlice(idx, window):
    return data[simIteration]["positions"][idx : idx + int(window)]


def getTimepointAtIndex(idx):
    return data[simIteration]["timepoints"][idx]


def setSimIteration(val):
    simIteration = val
    