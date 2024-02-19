# Fichier créé par Axel COUDROT le 22/01/2024
# app/routes.py

from flask import render_template, flash, redirect, Response, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug import Response

from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from urllib.parse import urlsplit
from datetime import datetime


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():
    # user = {'username': 'Toi'}
    # return render_template('index.html', title='Page principale', user=user)
    # posts = [
    #    {
    #        'author': {'username': 'John'},
    #        'body': "Flask, c'est super !"
    #    },
    #    {
    #        'author': {'username': 'Suzan'},
    #        'body': "C'est encore mieux que Symfony ! Oups !"
    #    }
    # ]
    return render_template('index.html', title='Accueil')


@app.route('/apropos')
def a_propos():
    return render_template('apropos.html', title='A propos')


@app.route('/login', methods=['GET', 'POST'])
def login() -> Response | str:
    if current_user.is_authenticated:
        return redirect(url_for('/index'))
    form = LoginForm()
    if form.validate_on_submit():
        _user = User.query.filter_by(username=form.username.data).first()
        if _user is None or not _user.check_password(form.password.data):
            flash('Utilisateur ou mot de passe non valide.')
            return redirect(url_for('login'))
        login_user(_user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Enregistrement', form=form)


@app.route('/logout')
def logout() -> Response:
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register() -> Response | str:
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Bravo ! Vous devenez un nouvel utilisateur !')
        return redirect(url_for('login'))
    return render_template('register.html', title="S'enregistrer", form=form)


@app.route('/user/<username>')
@login_required
def user(username: str) -> str:
    user_ = User.query.filter(User.username == username).first_or_404(description="L'utilisateur saisi n'existe pas")
    return render_template('user.html', user=user_, posts=user_.posts)
