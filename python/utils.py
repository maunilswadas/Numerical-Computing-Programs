import math

def func1(x):
    return math.pow(x, 2) - 4

def func2(x):
    return -(math.pow(x, 2)) + 4 * x + 5

def func3(x):
    return math.pow(x, 3) - 3 * math.pow(x, 2) - 9 * x - 10

def func4(x):
    return math.pow(x, 2) -2 * x + 3

def func5(x):
    return 2 * math.pow(x, 3) - 10 * math.pow(x, 2) + 11 * x - 5 

def func6(x):
    return math.exp(-x) - x

def func7(x):
    return x - math.exp(1 / x)

def function_points(f):
    x_points = []
    y_points = []
    for x in range(-100, 100):
        if x == 0: continue
        x_points.append(x / 10)
        y_points.append(f(x / 10))
    return (x_points, y_points)

def select_function(number):
    if number == 0:
        return func1
    if number == 1:
        return func2
    if number == 2:
        return func3
    if number == 3:
        return func4
    if number == 4:
        return func5
    if number == 5:
        return func6
    if number == 6:
        return func7
    return func1

