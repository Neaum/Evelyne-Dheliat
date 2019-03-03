DEVELOPPEMENT D'UNE STATION METEO

Pour ce projet nous nous sommes servis du capteur DHT11 et de l'ESP8266.
Une vue d'ensemble explicative est represent�e sur la Figure1 (cf github)


Le capteur DHT11 reli� au module Lolin mesure la temp�rature et l'humidit� toutes les 5 secondes. L'antenne reli�e au module envoi les donn�es (en hexad�cimal) � sigfox.

Branchement des modules :
- Alimentation du capteur en 3V
- Donn�es re�u sur le pin D1 de l'ESP
- Alimentation de l'antenne en 3V
- TX Branch� sur le pin D7
- RX branch� sur le pin D8

Nous tra�ons ensuite les courbes � l'aide de la libairie Morris.js
Nous faisons une moyenne des donn�es sur la journ�e et on affiche les 7 derniers jours sur le graphique.

Nous avons mis en place 2 serveurs (1 client, 1 fournisseur)

dessin explicatof du projet (fig 1 loic)

Une fois les messages (datas temp et hum) envoy� par sigfox via le Lolin, on les recupere en configurant un callback via l'interface propos� par le backend de sigfox.
Ce callback contient donc l'id du device et �galement les datas de temp�rature. Ces datas sont ensuite recuperer via la cr�ation d'un tunnel ngrok vers le localhost du PC 1.
Cela permet de r�cuperer via un programme python flask donn� par le prpfesseur Monsieur Triboux ces datas et de les envoyer via mqtt vers le PC2

Le PC 2 va traiter ces donn�es et les traduire en float pour avoir les valeurs r�elles de la temp�rature et de l'humidit�.
Il va ensuite mettre � jour une database en local (simul� via un .txt : meteo.txt) qui suit l'�volution de l'humidit� et de la temp�rature sous les 7 jours.
Une page web vient ensuite r�cuperer ses donn�es et les afficher via un graphique sur une interface via un serveur wamp tout en affichant �galement les donn�es actuelles.
Le graphiqe est fait aled de la librairie morris.js
