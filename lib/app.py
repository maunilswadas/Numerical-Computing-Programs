from flask import Flask, jsonify, request
from flask_cors import CORS
from regression import regression
import json

app = Flask(__name__)
CORS(app)

@app.route('/regression')
def func1():
    points = json.loads(request.args.get('points'))
    degree = int(request.args.get('degree'))
    return jsonify(regression(points,degree))

if __name__ == '__main__':
   app.run()
