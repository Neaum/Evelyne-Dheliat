from flask import Flask
from flask import request
from flask import jsonify
import time
import paho.mqtt.publish as mqtt


app = Flask(__name__)


@app.route("/", methods=['POST'])

def data():
	body = request.json
	if body == None:
		return "not a json"
	if 'data' in body.keys():
		mqtt.single(body["data"])		##Envoi des datas via MQTT vers PC 2


	return jsonify(body)

app.run(debug=True)

data()
