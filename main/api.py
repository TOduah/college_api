from flask import Flask, render_template 
from flask import request, jsonify 
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
    # f = open('collegesdata.json',)

    # data = json.load(f)
    
    # for i in data:
    #     print(i)
    # f.close()

     

# @app.route('/api/v1/resources/book/<string:name>', methods=['GET'])
# def home(name):



app.run()


