# Projet Wi-fi UHA

## Synopsis
Le projet Wi-Fi UHA consiste à analyser les données relatives à l'enregistrement de la puissance du signal Wi-Fi généré par les points d'accès dans le bâtiment C. 

## Données
Les données obtenus à partir du Fipy Pycomm et ont été sauvegardées dans le dossier *data/raw*. Il contient deux dossiers l'un relatif à une série de mesures effectuées au rez-de-chaussée du bâtiment C, l'autre à une série de mesure au premier étage du bâtiment C. 

## Tâches
Les tâches demandées dans ce projet sont les suivantes.

1. Compléter le programme src/data/extract-data.py afin de formater le jeux de données dans un fichier csv.
2. Écrire un programme qui fusionne deux fichiers csv.
3. Établir pour chaque variable le nombre de valeurs manquantes et aberrante ainsi que le pourcentage que cela représente.
4. Établir le nombre et le pourcentage d'observations qui ont des valeurs aberrantes et/ou manquantes.
5. Définir les fonctions ComputeMean et ComputeMedian (*src/model/model.py*) et calculer la moyenne et la médiane de la puissance du signal Wi-Fi du réseau UHA à chaque emplacement où les mesures ont été effectuées.
6. Afficher la heatmap de la puissance du signal Wi-Fi du réseau UHA en fonction des positions où les mesures ont été effectués



