# Fichier créé par Axel COUDROT le 05/02/2024
# app/config.py
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'un mot de passe à garder secret'
