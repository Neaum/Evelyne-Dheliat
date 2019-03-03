import datetime
import os.path
import paho.mqtt.client as mqtt
from statistics import mean

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    valeur=str(msg.topic)
    tem=valeur[:2]
    hu=valeur[2:]
    date = datetime.datetime.now().isoformat()
    realdate = date.split("T")
    realdate="'"+realdate[0]+"'"
    temp=int(tem,16)
    hum=int(hu,16)
    fr=open("meteo.txt","r")
    contenu=""
    j=0
    for lignes in fr:
        if(j==0):
            old=lignes
        elif(j!=6):
            contenu+=lignes
        elif(j==6):
            lastdate=lignes.split(" ")
            lastligne=lignes
        j=j+1
    fr.close()
    f = open("meteo.txt","w")
    if(lastdate[1]==str(0)):   #Data on other  day
        print("newd")
        f.write(contenu)
        f.write(lastligne)
        f.write(realdate+" "+str(temp)+" "+str(hum)+"\n")    #Add new data
        list_temp[:]=[]
        list_hum[:]=[]
        list_temp.append(float(temp))
        list_hum.append(float(hum))
    elif(lastdate[0] != realdate):  #Still the init data
        print("newi")
        f.write(contenu)
        f.write(lastligne)
        f.write(realdate+" "+str(temp)+" "+str(hum)+"\n")    #Add new data
        list_temp[:]=[]
        list_hum[:]=[]
        list_temp.append(float(temp))
        list_hum.append(float(hum))
    else:   #Data on the same day
        print("old")
        list_temp.append(float(temp))
        list_hum.append(float(hum))
        f.write(old)
        f.write(contenu)
        f.write(realdate+" "+str(mean(list_temp))+" "+str(mean(list_hum))+"\n")
    f.close()

#init .txt database
if(os.path.isfile("meteo.txt")==False):
    f = open('meteo.txt', 'a')
    for i in range(0,7):
        f.write("'"+(datetime.datetime.now().isoformat()).split("T")[0]+"'"+" "+str(0)+" "+str(0)+"\n")
    f.close()
valeur=""
list_temp=[]
list_hum=[]
client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("192.168.1.10",1883,60)
client.loop_forever()
