from random import uniform
from math import sqrt, log, exp, e

def nextCentral(stddev, mean):
    total = 0
    for j in range(12): total += uniform(0, 1)
    
    return stddev*(total - 6) + mean


nextPolarProps = {
    "haveNextPolar": False,
    "nextPolar": 0
}

def nextPolar(stddev, mean):
    if nextPolarProps["haveNextPolar"]: 
        nextPolarProps["haveNextPolar"] = False
        return nextPolarProps["nextPolar"]
    
    u1 = 2*uniform(0, 1) - 1
    u2 = 2*uniform(0, 1) - 1
    r = u1*u1 + u2*u2
    while r >= 1:
        u1 = 2*uniform(0, 1) - 1
        u2 = 2*uniform(0, 1) - 1
        r = u1*u1 + u2*u2
       
    factor = stddev * sqrt(-2 * log(r)/r)

    v1 = factor*u1 + mean
    v2 = factor*u2 + mean
    
    nextPolarProps["nextPolar"] = v1
    nextPolarProps["haveNextPolar"] = True
    return v2


C1 = sqrt(8/e)
C2 = 4*exp(0.25)
C3 = 4*exp(-1.35)

def nextRatio(stddev, mean):
    x = 0

    while True:
        u = uniform(0, 1)
        while (u == 0):
            u = uniform(0, 1)
        v = uniform(0, 1)
        y = C1 * (v - 0.5)
        x = y/u

        xx = x*x;
        if not((xx > 5 - C2*u) and ( xx >= C3/u + 1.4 or xx > -4*log(u))):
            break

    return stddev*x + mean