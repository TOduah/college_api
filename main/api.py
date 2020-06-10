from flask import Flask, render_template 
from flask import request, jsonify 

app = Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)

# @app.route('/api/v1/resources/book/<string:name>', methods=['GET'])
# def home(name):



app.run()


