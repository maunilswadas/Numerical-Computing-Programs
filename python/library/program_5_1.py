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

def bisection(func, x_min, x_max, tolerance = 0.0001, maximum_iterations = 20):
	function = func1
	if func == 1:
		function = func1
	if func == 2:
		function = func2
	if func == 3:
		function = func3
	if func == 4:
		function = func4
	if func == 5:
		function = func5
	if func == 6:
		function = func6
	if func == 7:
		function = func7

	function_points = []
	for x in range(math.floor(x_min * 10) - 10, math.ceil(x_max * 10) + 10):
		function_points.append([x/10, function(x/10)])

	steps = []

	if(x_min < x_max and function(x_min) < 0 and function(x_max) > 0 or function(x_min) > 0 and function(x_max) < 0):
		x_middle = (x_min + x_max) / 2
	
		for interation in range(0, maximum_iterations):
			x_middle = (x_min + x_max) / 2
			steps.append([x_min,x_max,x_middle])
			# print(interation, "x:", x_middle,"    f(x):", function(x_middle))
			if(function(x_middle) == 0 or (x_max - x_min) / 2 < tolerance):
				return { "steps": steps, "function_points": function_points}
            
			if(function(x_min) * function(x_middle) > 0):
				x_min = x_middle
			else:
				x_max = x_middle


		return { "steps": steps, "function_points": function_points}
