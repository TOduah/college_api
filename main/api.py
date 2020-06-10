from flask import Flask 
from flask import request, jsonify 

app = Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return "<p>Hello, world!</p>"

# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     return jsonify(books)



app.run()


