import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import data
import functions as fn
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def home():
    return "<h1>BikeShare Project API</h1>"

@app.route('/api/chicago', methods=['GET'])
@cross_origin()
def api_chicago():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))
    if not months or not days:
        return "Months and Days are required", 400
    else:
        return jsonify(fn.execute_analysis('chicago', months, days))

@app.route('/api/washington', methods=['GET'])
@cross_origin()
def api_washington():
    return jsonify(data.chicago)

@app.route('/api/newyork', methods=['GET'])
@cross_origin()
def api_newyork():
    return jsonify(data.chicago)

app.run()