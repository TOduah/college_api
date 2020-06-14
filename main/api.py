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

# endpoint for specific college
@app.route('/api/v1/colleges/<string:college_name>', methods=['GET'])
def get_college(college_name):
    with open('data/collegesdata.json', 'r') as f:
        data = json.load(f)

    for college in data:
        if college_name in college["college-name"]:
            return jsonify(college)
    return None

# endpoint for colleges of a specific academic-calendar
@app.route('/api/v1/colleges/calendar/<string:calendar>', methods=['GET'])
def get_calendar(calendar):
    with open('data/collegesdata.json', 'r') as f:
        data = json.load(f)
    c_list = []

    for c in data:
        if c["academic-calendar"] == calendar:
            c_list.append(c)

    return jsonify(c_list)

# endpoit for colleges of a specific campus-setting
@app.route('/api/v1/colleges/setting/<string:setting>', methods=['GET'])
def get_setting(setting):
    with open('data/collegesdata.json', 'r') as f:
        data = json.load(f)
    s_list = []

    for s in data:
        if s["campus-setting"] == setting:
            s_list.append(s)

    return jsonify(s_list)



app.run()


