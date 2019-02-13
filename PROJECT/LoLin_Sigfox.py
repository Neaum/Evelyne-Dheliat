from flask import Flask
from flask import request
from flask import jsonify
import paho.mqtt.publish as mqtt
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
        #receive_data temperature and humidity
        Temp=str(getTemp())
        Hum = str(getHum())
        #creation message mqtt to send
        MESSAGE=Temp+" "+Hum
        print(MESSAGE)
        #send message
        mqtt.single("Value",MESSAGE)
    return jsonify(body)

app.run(debug=False)
