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
        return jsonify(fn.execute_analysis(fn.get_df('chicago', months, days)))

@app.route('/api/washington', methods=['GET'])
@cross_origin()
def api_washington():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))
    if not months or not days:
        return "Months and Days are required", 400
    else:
        return jsonify(fn.execute_analysis(fn.get_df('washington', months, days)))

@app.route('/api/newyork', methods=['GET'])
@cross_origin()
def api_newyork():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))
    if not months or not days:
        return "Months and Days are required", 400
    else:
        return jsonify(fn.execute_analysis(fn.get_df('new_york_city', months, days)))

# Users

@app.route('/api/chicago/users', methods=['GET'])
@cross_origin()
def api_chicago_users():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))
    start = int(json.loads(request.args.get('start')))
    end = int(json.loads(request.args.get('end')))

    df = fn.get_df('chicago', months, days)
    users = fn.getUsers(df, start, end).to_json(orient='index')
    parsed_users = json.loads(users)
    return parsed_users

@app.route('/api/washington/users', methods=['GET'])
@cross_origin()
def api_washington_users():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))
    start = int(json.loads(request.args.get('start')))
    end = int(json.loads(request.args.get('end')))
    
    df = fn.get_df('washington', months, days)
    print(df.head())
    users = fn.getUsers(df, start, end).to_json(orient='index')
    parsed_users = json.loads(users)
    return parsed_users

@app.route('/api/newyork/users', methods=['GET'])
@cross_origin()
def api_newyork_users():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))
    start = int(json.loads(request.args.get('start')))
    end = int(json.loads(request.args.get('end')))
    
    df = fn.get_df('new_york_city', months, days)
    users = fn.getUsers(df, start, end).to_json(orient='index')
    parsed_users = json.loads(users)
    return parsed_users