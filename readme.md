# Projet Wi-fi UHA

## Programme:

### Installation
Cloner le repo (avec clef SSH):
```bash
git clone git@github.com:ldsvrn/sae15-wifi.git
```

Créer l'environnement virtuel:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 -r requirements.txt
```

Mettre à jour le fichier requirements.txt:
```bash
pip3 freeze > requirements.txt
```

### Utilisation:
Parser pour extraire les données brutes:
```bash
src/data/extract-data.py -i *path raw dataset* -o *csv output path*
```

Script pour fusionner les csv et trier par ExpId:
```bash
src/data/merge-csv.py -i *csv dataset folder* -o *merged csv*
```

## Sujet:

### Synopsis
Le projet Wi-Fi UHA consiste à analyser les données relatives à l'enregistrement de la puissance du signal Wi-Fi généré par les points d'accès dans le bâtiment C. 

### Données
Les données obtenus à partir du Fipy Pycomm et ont été sauvegardées dans le dossier *data/raw*. Il contient deux dossiers l'un relatif à une série de mesures effectuées au rez-de-chaussée du bâtiment C, l'autre à une série de mesure au premier étage du bâtiment C. 

### Tâches
Les tâches demandées dans ce projet sont les suivantes.

1. Compléter le programme src/data/extract-data.py afin de formater le jeux de données dans un fichier csv.
2. Écrire un programme qui fusionne deux fichiers csv.
3. Établir pour chaque variable le nombre de valeurs manquantes et aberrante ainsi que le pourcentage que cela représente.
4. Établir le nombre et le pourcentage d'observations qui ont des valeurs aberrantes et/ou manquantes.
5. Définir les fonctions ComputeMean et ComputeMedian (*src/model/model.py*) et calculer la moyenne et la médiane de la puissance du signal Wi-Fi du réseau UHA à chaque emplacement où les mesures ont été effectuées.
6. Afficher la heatmap de la puissance du signal Wi-Fi du réseau UHA en fonction des positions où les mesures ont été effectués



