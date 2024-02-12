# Projet Flask

## Author
Axel COUDROT : axel.coudrot@free.fr

## Mise en place du projet

### Mise en place de git
```bash
git clone https://iut-info.univ-reims.fr/gitlab/coud0011/flask.git
```

À chaque modification que vous effectuez : 
```
git add .
git commit -m "Message du commit"
git push
```
À chaque modification effectuée par quelqu'un d'autre
```bash
git pull
```

### Installation de l'environnement
*Mise en place valable sous linux uniquement, pour Windows, c'est en cours*
- Mise à jour de vos sources d'application linux
```bash
sudo apt update
```
- Installation de python 3
```bash
sudo apt install python3
```
- Installation de pip
```bash
sudo apt install python3-pip
```
- Mise en place de l'environnement de développement pour flask
```bash
python3 -m venv env_flask
```
- Installation de l'ensemble des packages requis pour le projet
```bash
pip install -r requirements.txt
```
## Création de la base de donnée
Sous Linux : 
```bash
/bin/bash /working/coud0011/archilogiciel/flask/app/init.sh
```
Sous Windows : 
```
Mise en place en cours
```