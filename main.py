from agents.randomwalk import randomwalk1D
from utils.graph import linePlots

start = {
  't': 0,
  'x': 1.0
}

limit = {
  'min': -1.0,
  'max': +1.0
}

size = 10
runs=[]
for i in range(0,10):
    runs.append(randomwalk1D(start, limit, size))

linePlots(runs, 'time', 'value', '1D Random Walk Runs')