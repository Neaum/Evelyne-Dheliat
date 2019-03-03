Projet IOT
==

DE Loïc Tang, Hugo Savard, Zoé Moulart, Lefebvre Samuel. 


Description Projet
--
### Schéma de principe:
![figure_1](principle_scheme.png)


### Partie capteur:

Pour ce projet nous nous sommes servis dans un premier temps du capteur DHT11 et de l'ESP8266.

Le capteur DHT11 relié au module Lolin mesure la température et l'humidité toutes les 5 secondes. L'antenne reliée au module envoi les données (en hexadécimal) à sigfox.

Branchement des modules :
* Alimentation du capteur en 3V
* Données reçu sur le pin D1 de l'ESP
* Alimentation de l'antenne en 3V
* TX Branché sur le pin D7
* RX branché sur le pin D8


Un premier programme sur Arduino (Capteur_2.ino) permet de récuperer les valeurs de température et d'humidité du capteur et de les envoyer vers le backend de Sigox.

### Partie Serveurs

Dans un second temps, nous avons configuer le backend de SigFox (https://backend.sigfox.com/) afin de créer un callbacks permettant de generer un message json contenant l'id du device Lolin et les datas de températures.

Ainsi, une fois le message contenant les datas envoyés, nous pouvons les récuperer directement sur un premier PC passerelle via Ngrok et un script python (LoLin_Sigfox.py). Nous allons ensuite envoyer ces données via un serveur mqtt vers un autre PC qui permet l'affichage de l'interface utilisateur et la mise à jour de la database meteo.txt.

Le PC 2 va donc traiter ces données et les traduire afin d'avoir des données compréhensible par l'utilisateur (càd en float et non en hex).
Il va ensuite mettre à jour une database en local (simulé via un .txt : meteo.txt) qui suit l'évolution de l'humidité et de la température sous les 7 jours.
Une page web (Station_Meteo.php) vient ensuite récupérer ces données et les afficher via un graphique sur une interface web via un serveur wamp tout en affichant également les données actuelles.
Le graphiqe est fait à l'aide de la librairie morris.js

Technologies Utilisés:
- mqtt
- Sigfox
- Ngrok
- Arduino IDE
- Python
- WampServer


Fonctionnement
--

Afin de procéder au bon fonctionnement du programme, il faut suivre ces quelques étapes afin de bien régler les différentes composantes du projet:

**Sur un premier PC-0:**
1. Effectuer les branchements cités au-dessus
2. Lancer le programme arduino Capteur_2.ino en notant l'id du device qui s'affiche sur la console

**Sur un deuxième PC-1:**
1. Lancer un serveur mosquitto et récuperer l'adresse IP de ce PC
2. Lancer également Ngrok, et dans l'invite de commande qui apparait executer la commande : **ngrok http 5000 -region eu**
3. Aller sur le site: https://backend.sigfox.com/
4. Trouver votre device id et créer un nouveau callback: 
![fig_2.png](fig_2.png)

3. Lancer ensuite le programme LoLin_Sigfox.py

**Sur un troisième PC-3:**
1. Lancer WampServer
2. 

Lancer le programme WriteSql.py en ayant au préalable modifier l'adresse IP avec celle récuperer avant à la ligne 75
2. 
