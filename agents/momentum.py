from agents.agent import Agent

class MomentumAgent(Agent):
    def __init__(self):
      super(MomentumAgent, self).__init__()
      self.b = 2

    def do(self, b):
        print(self.a + b)