from math import exp

MAX_ITERS = 50
TOLERANCE = 0.001

class FixedPointRootFinder:
    def __init__(self,func):
        self.xn = None
        self.prev_xn = None
        self.gn = None
        self.func = func
        self.n = 0
    
    def computeNextPosition(self):
        self.prevXn = self.xn
        self.xn     = self.gn
        self.gn     = self.func(self.xn)
    
    def hasConverged(self):
        return abs((self.gn - self.xn) / self.xn) < TOLERANCE or self.n > MAX_ITERS - 1
    
    def step(self):
        self.computeNextPosition()
        self.n += 1
        return self.hasConverged()
        
    
    def reset(self, x0):
        self.gn = x0
        self.n = 0