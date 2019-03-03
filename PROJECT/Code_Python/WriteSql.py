import datetime
import os.path
import paho.mqtt.client as mqtt
from statistics import mean

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("#")

def on_message(client, userdata, msg):      #Sur reception d'un message
    print(msg.topic+" "+str(msg.payload))       #Affichage du message
    valeur=str(msg.topic)                       #Recuperation et traitement des data : ex: 1527=>temp=15,hum=27=>temp=21,hum=39
    tem=valeur[:2]
    hu=valeur[2:]
    date = datetime.datetime.now().isoformat()  #Recuperation de l'heure d'arrivée du message
    realdate = date.split("T")
    realdate="'"+realdate[0]+"'"
    temp=int(tem,16)
    hum=int(hu,16)
    fr=open("meteo.txt","r")
    contenu=""
    j=0
    for lignes in fr:                       #Mise à jour de la database meteo.txt
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
    if(lastdate[1]==str(0)):   #Si la database n'a pas était déjà rempli
        #print("newd")
        f.write(contenu)
        f.write(lastligne)
        f.write(realdate+" "+str(temp)+" "+str(hum)+"\n")    #Add new data
        list_temp[:]=[]
        list_hum[:]=[]
        list_temp.append(float(temp))
        list_hum.append(float(hum))
    elif(lastdate[0] != realdate):  #Si le message ne concerne pas le même jour que la derniere valeur ajoutée
        #print("newi")
        f.write(contenu)
        f.write(lastligne)
        f.write(realdate+" "+str(temp)+" "+str(hum)+"\n")    #Add new data and delete last line
        list_temp[:]=[]
        list_hum[:]=[]
        list_temp.append(float(temp))
        list_hum.append(float(hum))
    else:   #Si le message concerne le même que la dernière valeur ajoutée
        #print("old")
        list_temp.append(float(temp))   #On calcule la moyenne de température et d'humidité
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

valeur=""   #init variable
list_temp=[]    #liste contenant les différentes valeurs de température sur une meme journée
list_hum=[]     #idem avec l'humidité

client=mqtt.Client()    #création du broker mqtt
client.on_connect=on_connect
client.on_message=on_message
client.connect("192.168.1.10",1883,60)
client.loop_forever()
