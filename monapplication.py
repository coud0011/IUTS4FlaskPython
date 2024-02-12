# Fichier créé par Axel COUDROT le 22/01/2024
# monapplication.py

from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
