from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import json
import os
import main
# //https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
# https://stackoverflow.com/questions/52033852/python-flask-how-to-convert-a-dictionary-object-to-json

# init app
app = Flask(__name__)


# routes
@app.route('/chat', methods=['POST', 'GET'])
def chat():
    req = request.json
    print("below is req")
    print(req)

    return jsonify({"response": main.chat(req)})


# run server
if __name__ == '__main__':
    app.run(debug=True)
