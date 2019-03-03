<!DOCTYPE html>
<html lang="fr">
	<head>
		<title>Station Meteo</title>
	  <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
	  <script src="http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.2/raphael-min.js"></script>
	  <script src="../morris.js"></script>
	  <script src="http://cdnjs.cloudflare.com/ajax/libs/prettify/r224/prettify.min.js"></script>
	  <script src="lib/example.js"></script>
	  <link rel="stylesheet" href="lib/example.css">
	  <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/prettify/r224/prettify.min.css">
	  <link rel="stylesheet" href="../morris.css">
	</head>
	<body>
		<?php
            //Ouverture Fichier
			$dates=array();
			$temp=array();
			$hum=array();
            $monfichier = fopen('D:/Bureau/meteo.txt', 'r+');

            //Traitement
            for ($i = 0; $i <7; $i++) {
                $ligne = fgets($monfichier);
                $mots=explode(" ", $ligne);
                array_push($dates, $mots[0]);
                array_push($temp, $mots[1]);
                array_push($hum, $mots[2]);
            }
            //Fermeture Fichier
            fclose($monfichier);
        ?>
		<h1>Température et Humidité sur les 7 derniers jours</h1>
		<div id="graph"></div>
		<div id="id_div_1" style="display:none;">
			<pre id="code" class="prettyprint linenums">
			Morris.Line({
			  element: 'graph',
			  data: [
			    {x: <?php echo $dates[0]?>, y: <?php echo (int)$hum[0]?>, z: <?php echo (int)$temp[0]?>},
			    {x: <?php echo $dates[1]?>, y: <?php echo (int)$hum[1]?>, z: <?php echo (int)$temp[1]?>},
			    {x: <?php echo $dates[2]?>, y: <?php echo (int)$hum[2]?>, z: <?php echo (int)$temp[2]?>},
			    {x: <?php echo $dates[3]?>, y: <?php echo (int)$hum[3]?>, z: <?php echo (int)$temp[3]?>},    
			    {x: <?php echo $dates[4]?>, y: <?php echo (int)$hum[4]?>, z: <?php echo (int)$temp[4]?>},
			    {x: <?php echo $dates[5]?>, y: <?php echo (int)$hum[5]?>, z: <?php echo (int)$temp[5]?>},
			    {x: <?php echo $dates[6]?>, y: <?php echo (int)$hum[6]?>, z: <?php echo (int)$temp[6]?>},
			  ],
			  xkey: 'x',
			  ykeys: ['y', 'z'],
			  labels: ['Humidité', 'Température']
			}).on('click', function(i, row){
			  console.log(i, row);
			});
			</pre>
		</div>
	</body>
</html>
