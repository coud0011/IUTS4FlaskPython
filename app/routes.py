# Fichier créé par Axel COUDROT le 22/01/2024
# app/routes.py
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index() -> str:
    user = {'username': 'Philippe'}
    return render_template('index.html', title='Page principale', user=user)
