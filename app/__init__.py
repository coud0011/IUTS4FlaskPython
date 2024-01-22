# Fichier créé par Axel COUDROT le 22/01/2024
# app/__init__.py
from flask import Flask

# Création de l’application
app = Flask(__name__)
# On importe le fichier contenant
# la définition des fonctions de vue
from app import routes
# tailwind css
