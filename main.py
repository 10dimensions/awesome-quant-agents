from agents.randomwalk import randomwalk1D
from utils.graph import linePlots


def func1():
    # start value and randomness limit
    start = { 't': 0, 'x': 1.0 }
    limit = { 'min': -1.0, 'max': +1.0 }

    runs = 1000
    dat=[]
    for i in range(0,10):
        dat.append(randomwalk1D(start, limit, runs))
    
    linePlots(dat, 'time', 'value', '1D Random Walk Runs')


if __name__ == "__main__":
    func1()