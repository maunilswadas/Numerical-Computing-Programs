from math import exp
class Functions:
    def __init__(self):
        self.items = {
            "0": {
                "eq": lambda x: pow(x,2) - 4,
                "eq_diff": lambda x,y:  2*x,
                "init":(2, 0),
                "x":6
            },
            "1": {
                "eq": lambda x: pow(x,3) + 3*pow(x,2) - 9*x - 10,
                "eq_diff": lambda x,y:  3*pow(x,2) + 6*x - 9,
                "init":(-4.5050397, 0),
                "x":6
            },
            "2": {
                "eq": lambda x: 2*pow(x,3) - 10*pow(x,2) + 11*x - 5,
                "eq_diff": lambda x,y:  6*pow(x,2) - 20*x + 11,
                "init":(0,-5),
                "x":6
            },
            "3": {
                "eq": lambda x: 3*exp(x) + 2*exp(2*x)*(x - 1),
                "eq_diff": lambda x,y: 2*x*exp(2*x) + y,
                "init":(0,1),
                "x":6
            },
            "4": {
                "eq": lambda x: 4*x - 3*exp(-2*x) + 2,
                "eq_diff": lambda x,y: 8*x - 2*y + 8,
                "init":(0,-1),
                "x":6
            },
            "5": {
                "eq": lambda x: ((x*x - 1)*exp(-2*x))/2,
                "eq_diff": lambda x,y: x*exp(-2*x) - 2*y,
                "init":(0, -0.5),
                "x":6
            }
        }
        self.current = "0"
    
    def currnet_func(self):
        return self.items[self.current]

    
def eulers_diff_eq_solver(x, y, h, eq_diff):
    return(x + h, y + h*eq_diff(x,y))

def predictor_corrector_diff_eq_solver(x, y, h, eq_diff):
    predictor = y + abs(h)*eq_diff(x,y)
    avgSlope = (eq_diff(x, y) + eq_diff(x+h, predictor))/2
    return (x + h, y + h*avgSlope)

def runge_kutta_diff_eq_solver(x, y, h, eq_diff):
    k1 = eq_diff(x, y)
    k2 = eq_diff(x + h/2, y + k1*h/2)
    k3 = eq_diff(x + h/2, y + k2*h/2)
    k4 = eq_diff(x + h, y + k3*h)
    return (x + h, y + (k1 + 2*(k2 + k3) + k4)*h/6)
