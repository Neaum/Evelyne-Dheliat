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
    temp=float(msg.payload.split()[0])
    hum=float(msg.payload.split()[1])

    c.execute("INSERT INTO data VALUES (?,?,?)", (date,temp,hum) )
    conn.commit()


# conn = sqlite3.connect('dataMeteo.db')
# c = conn.cursor()
# client=mqtt.Client()
# client.on_connect=on_connect
# client.on_message=on_message
# client.connect("192.168.43.136",1883,60)
# client.loop_forever()
string = "2019-03-05T 8A27648124"
print(string)
realdate=string.split("T")
f = open("meteo.txt","a")
f.write("'"+realdate[0]+"\n")
f.close()
f = open("meteo.txt","a")
f.write("'"+"bite"+"'")
f.close()
#
# f = open("meteo.txt","w+")
# f.write(realdate)
# f.close()
