from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import datetime

app = Flask(__name__)

@app.route("/", methods=['POST'])
def data():
    body = request.json
    if body == None:
        return "not a json"
    if 'data' in body.keys():
        print("MessageRecu")
        #codeAPIpourrecup meteo
        #envoyer_reponse
    return jsonify(body)

app.run(debug=False)
