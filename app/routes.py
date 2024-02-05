# Fichier créé par Axel COUDROT le 22/01/2024
# app/routes.py

from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"L’utilisateur {form.username.data} est enregistré")
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)