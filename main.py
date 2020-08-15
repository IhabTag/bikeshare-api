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

# App Routes

@app.route('/', methods=['GET'])
def home():
    return "<h1>BikeShare Project API</h1>"

# Routes to fetch cities data

# Getting Chicago data filtered by months and days coming with the request as args
@app.route('/api/chicago', methods=['GET'])
@cross_origin()
def api_chicago():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))

    # Checking for months and days filters and return error response if not set
    if not months or not days:
        return "Months and Days are required", 400
    else:
        return jsonify(fn.execute_analysis(fn.get_df('chicago', months, days)))

# Getting Washington data filtered by months and days coming with the request as args
@app.route('/api/washington', methods=['GET'])
@cross_origin()
def api_washington():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))

    # Checking for months and days filters and return error response if not set
    if not months or not days:
        return "Months and Days are required", 400
    else:
        return jsonify(fn.execute_analysis(fn.get_df('washington', months, days)))

# Getting New York City data filtered by months and days coming with the request as args
@app.route('/api/newyork', methods=['GET'])
@cross_origin()
def api_newyork():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))

    # Checking for months and days filters and return error response if not set
    if not months or not days:
        return "Months and Days are required", 400
    else:
        return jsonify(fn.execute_analysis(fn.get_df('new_york_city', months, days)))

# Users data routes

# Getting 5 rows of Chicago data filtered by months and days coming with the request as args
@app.route('/api/chicago/users', methods=['GET'])
@cross_origin()
def api_chicago_users():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))

    # Start and End slicing args of the get get_users function
    start = int(json.loads(request.args.get('start')))
    end = int(json.loads(request.args.get('end')))

    df = fn.get_df('chicago', months, days)
    users = fn.get_users(df, start, end).to_json(orient='index')

    # Parsing users data as json object
    parsed_users = json.loads(users)
    return parsed_users

# Getting 5 rows of Washington data filtered by months and days coming with the request as args
@app.route('/api/washington/users', methods=['GET'])
@cross_origin()
def api_washington_users():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))

    # Start and End slicing args of the get get_users function
    start = int(json.loads(request.args.get('start')))
    end = int(json.loads(request.args.get('end')))
    
    df = fn.get_df('washington', months, days)
    print(df.head())
    users = fn.get_users(df, start, end).to_json(orient='index')

    # Parsing users data as json object
    parsed_users = json.loads(users)
    return parsed_users

# Getting 5 rows of New york City data filtered by months and days coming with the request as args
@app.route('/api/newyork/users', methods=['GET'])
@cross_origin()
def api_newyork_users():
    months = json.loads(request.args.get('months'))
    months = list(map(int, months))
    days = json.loads(request.args.get('days'))
    days = list(map(int, days))

    # Start and End slicing args of the get get_users function
    start = int(json.loads(request.args.get('start')))
    end = int(json.loads(request.args.get('end')))
    
    df = fn.get_df('new_york_city', months, days)
    users = fn.get_users(df, start, end).to_json(orient='index')

    # Parsing users data as json object
    parsed_users = json.loads(users)
    return parsed_users