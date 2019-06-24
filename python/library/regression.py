import numpy as np
import numpy.matlib
from numpy.linalg import inv

def regression(points, degree = 1):
    points = numpy.array(points)
    min_point = -9
    max_point = 9
    
    X = np.matlib.empty((degree + 1,degree + 1))
    Y = np.matlib.empty((degree + 1,1))

    X_elements = []
    for num in range(0,(degree + 1)*2 -1):
        X_elements.append(np.sum([np.power(point[0],num) for point in points]))

    offset = 0
    for row in range(0,degree + 1):
        end = offset + degree + 1
        X[row] = X_elements[offset:end]
        offset += 1

    for num in range(0,degree + 1):
        Y[num] = np.sum([np.power(point[0],num) * point[1] for point in points])
    
    X_inv = inv(X)
    coeff = X_inv.dot(Y)

    x = []
    y = []

    for i in range(min_point*20,max_point*20):
        x.append(i/20)
        y.append(np.sum([np.power(i/20,power)*ai[0] for power, ai in enumerate(coeff)]))

    return {"x":x, "y":y}

