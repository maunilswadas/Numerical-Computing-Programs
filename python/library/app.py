from flask import Flask, jsonify, request
from flask_cors import CORS
from regression import regression
from program_5_1 import bisection
from program_5_2 import regulaFalsi

import json

app = Flask(__name__)
CORS(app)

@app.route('/regression')
def func1():
    points = json.loads(request.args.get('points'))
    degree = int(request.args.get('degree'))
    return jsonify(regression(points,degree))

@app.route('/program_5_1')
def program_5_1():
    func = int(request.args.get('func'))
    x_min = float(request.args.get('x_min'))
    x_max = float(request.args.get('x_max'))
    maximum_iterations = int(request.args.get('maximum_iterations'))
    tolerance = float(request.args.get('tolerance'))
    return jsonify(bisection(func, x_min, x_max, tolerance, maximum_iterations))

@app.route('/program_5_2')
def program_5_2():
    func = int(request.args.get('func'))
    x_min = float(request.args.get('a'))
    x_max = float(request.args.get('b'))
    maximum_iterations = int(request.args.get('maximum_iterations'))
    tolerance = float(request.args.get('tolerance'))
    return jsonify(regulaFalsi(func, x_min, x_max, tolerance, maximum_iterations))


if __name__ == '__main__':
   app.run()
