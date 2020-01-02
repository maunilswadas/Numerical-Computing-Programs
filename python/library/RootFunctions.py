from math import exp, sqrt, log, sin
class Functions:
    def __init__(self):
        self.items = {
            "0": lambda x: (x + 4/x)/2,
            "1":  lambda x: 4/x,
            "2":  lambda x: sqrt(x+2),
            "3":  lambda x: 2/x + 1,
            "4":  lambda x: pow(x,2) - 2,
            "5":  lambda x: exp(-x),
            "6":  lambda x: -log(x),
            "7":  lambda x: exp(1/x),
            "8":  lambda x: 1/log(x),
            "9":  lambda x: (x + exp(1/x)) / 2,
            "10":  lambda x: sin(x)/2 + 1,
            "11":  lambda x: 1 + 1/x + 1/x*x,
            "12":  lambda x: (x*x + 2*x + 10)
        }
        self.current = "0"
    
    def currnet_func(self):
        return self.items[self.current]