from utils.math import randomWalk1D
from utils.graph import linePlots


#Sim Parameters
start = { 't': 0, 'x': 1.0 }
limit = { 'min': -1.0, 'max': +1.0 }
runs = 1000
totalIterations = 10
simIteration = 0

#Data store
data = []
datHash = None


def createPriceFeed():
    #Iterating 10 runs
    for i in range(0,totalIterations):
        rw = randomWalk1D(start, limit, runs)
        data.append(rw)


def getPriceAtIndex(idx):
    return data[simIteration]["positions"][idx]


#def getPriceAtTimepoint():


def getPriceFeedInterval():
    return len(data[simIteration]['timepoints'])


def getTimepointAtIndex(idx):
    return data[simIteration]["timepoints"][idx]


def setSimIteration(val):
    simIteration = val
    