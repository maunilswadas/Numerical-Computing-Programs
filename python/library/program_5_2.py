import math
import numpy as np

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

def regulaFalsi(func, a, b, tolerance = 0.0001, maximum_iterations = 20):
	f = func1
	if func == 1:
		f = func1
	if func == 2:
		f = func2
	if func == 3:
		f = func3
	if func == 4:
		f = func4
	if func == 5:
		f = func5
	if func == 6:
		f = func6
	if func == 7:
		f = func7

	function_points = []
	for x in range(math.floor(a * 10) - 10, math.ceil(b * 10) + 10):
		function_points.append([x/10, f(x/10)])

	steps = []

	for i in range(0, maximum_iterations):
		FA = f(a)
		
		p = (a * f(b) - b * f(a)) / (f(b) - f(a))
		FP = f(p)

		steps.append({"p1": [a, f(a)], "p2": [b, f(b)], "p_middle": [p, FP]})
		
		if(FP == 0 or np.abs(f(p)) < tolerance):
			break
		
		if(FA * FP > 0):
			a = p
		else:
			b = p
	return {"steps": steps ,"function_points": function_points}

