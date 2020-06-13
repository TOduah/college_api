from flask import Flask, render_template 
from flask import request, jsonify 
from pprint import pprint
import json


app = Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/usage', methods=['GET'])
def usage():
    return render_template('usage.html')

# endpoint for all college data    
@app.route('/api/v1/colleges/all', methods=['GET'])
def api_all():
    with open('data/collegesdata.json', 'r') as f:
        data = json.load(f)

    return jsonify(data)

     

# @app.route('/api/v1/resources/book/<string:name>', methods=['GET'])
# def home(name):



app.run()


