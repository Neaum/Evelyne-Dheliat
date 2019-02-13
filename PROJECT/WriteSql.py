import sqlite3
import datetime
import os.path
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    date = datetime.datetime.now().isoformat()
    temp=float(msg.payload.split()[0])
    hum=float(msg.payload.split()[1])
    c.execute("INSERT INTO data VALUES (?,?,?)", (date,temp,hum) )
    conn.commit()

#Check if DB already exist, if not: create one
if os.path.isfile("dataMeteo.db"):
    print("DB already exists")
else:
    conn = sqlite3.connect('dataMeteo.db')
    c = conn.cursor()
    print("oui")
    c.execute('''CREATE TABLE data (date text, temp,humidity)''')


conn = sqlite3.connect('dataMeteo.db')
c = conn.cursor()
client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("192.168.43.136",1883,60)
client.loop_forever()
