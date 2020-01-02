from random import uniform
from math import sqrt, log, exp, e

def nextLog(mean):
    u = uniform(0, 1)
    while u == 0: u = uniform(0, 1)
        
    return (-mean*log(u));


def nextVonNeumann(mean):
    n = None
    k = 0
    u1 = None

    while True:
        n = 1
        u1 = uniform(0, 1)
        
        u = u1
        uprev = None
        
        while True:
            uprev = u
            u = uniform(0, 1)
            
            if u > uprev:
                if n&1 == 0:
                    return u1 + k
                else:
                    k += 1
                    break;
            n += 1