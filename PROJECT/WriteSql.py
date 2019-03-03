import datetime
import os.path
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    date = datetime.datetime.now().isoformat()
    realdate = date.split("T")
    temp=(msg.payload.split()[0])
    hum=(msg.payload.split()[1])
    f = open("meteo.txt","a")
    f.write("'"+realdate[0]+"'"+" "+str(temp.decode("utf-8"))+" "+str(hum.decode("utf-8"))+"\n")
    f.close()


client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("192.168.1.10",1883,60)
client.loop_forever()
