# Fichier créé par Axel COUDROT le 22/01/2024
# app/routes.py
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Toi'}
    # return render_template('index.html', title='Page principale', user=user)
    posts = [
        {
            'author': {'username': 'Axel'},
            'body': "Flask, c'est super !"
        },
        {
            'author': {'username': 'Suzan'},
            'body': "C'est encore mieux que Symfony ! Oups !"
        }
    ]
    return render_template('index.html', title='Accueil', user=user, posts=posts)


@app.route('/apropos')
def a_propos():
    return render_template('apropos.html', title='A propos')
