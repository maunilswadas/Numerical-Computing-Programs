from math import floor
class Buckets:
    MAX_BAR_SIZE = 50
    
    def __init__(self, n):
        self.n = n
        self.counters = [0]*n
        self.rMin  = 0
        self.rMax  = 0
        self.width = 0
    
    def reset(self):
        self.counters = [0]*self.n
    
    def get(self, i):
        return self.counters[i]
    
    def get_bucket(self, i):
        return self.counters
    
    def setLimits(self, rMin, rMax):
        self.rMin  = rMin
        self.rMax  = rMax
        self.width = (rMax - rMin)/self.n

    def put(self, r):
        if r < self.rMin or r > self.rMax: return self.counters

        i = floor((r - self.rMin)/self.width)
        self.counters[i] += 1
        return self.counters
        
    def print_buckets(self):
        maxCount = 0;
        for i in range(self.n):
            maxCount = max(maxCount, self.counters[i])

        factor = Buckets.MAX_BAR_SIZE/maxCount

        for i in range(self.n):
            b = self.counters[i]

            length = round(factor*b)
            temp = ""
            for j in range(length): temp += "*"
            print(i, b, temp)