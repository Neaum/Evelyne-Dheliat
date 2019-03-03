DEVELOPPEMENT D'UNE STATION METEO

Pour ce projet nous nous sommes servis du capteur DHT11 et de l'ESP8266.
Une vue d'ensemble explicative est representée sur la Figure1 (cf github)


Le capteur DHT11 relié au module Lolin mesure la température et l'humidité toutes les 5 secondes. L'antenne reliée au module envoi les données (en hexadécimal) à sigfox.

Branchement des modules :
- Alimentation du capteur en 3V
- Données reçu sur le pin D1 de l'ESP
- Alimentation de l'antenne en 3V
- TX Branché sur le pin D7
- RX branché sur le pin D8

Nous traçons ensuite les courbes à l'aide de la libairie Morris.js
Nous faisons une moyenne des données sur la journée et on affiche les 7 derniers jours sur le graphique.

Nous avons mis en place 2 serveurs (1 client, 1 fournisseur)

dessin explicatof du projet (fig 1 loic)

Une fois les messages (datas temp et hum) envoyé par sigfox via le Lolin, on les recupere en configurant un callback via l'interface proposé par le backend de sigfox.
Ce callback contient donc l'id du device et également les datas de température. Ces datas sont ensuite recuperer via la création d'un tunnel ngrok vers le localhost du PC 1.
Cela permet de récuperer via un programme python flask donné par le prpfesseur Monsieur Triboux ces datas et de les envoyer via mqtt vers le PC2

Le PC 2 va traiter ces données et les traduire en float pour avoir les valeurs réelles de la température et de l'humidité.
Il va ensuite mettre à jour une database en local (simulé via un .txt : meteo.txt) qui suit l'évolution de l'humidité et de la température sous les 7 jours.
Une page web vient ensuite récuperer ses données et les afficher via un graphique sur une interface via un serveur wamp tout en affichant également les données actuelles.
Le graphiqe est fait aled de la librairie morris.js
