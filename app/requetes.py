# Fichier créé par Axel COUDROT le 12/02/2024
from app import db, app
from app.models import User, Post
from datetime import datetime

app.app_context().push()

users = User.query.all()
for u in users:
    db.session.delete(u)
posts = Post.query.all()

for p in posts:
    db.session.delete(p)
db.session.commit()

users = [("John", "john@example.com"), ("Suzan", "suzan@example.com"), ("David", "david@example.com"),
         ("Alice", "alice@example.com")]
posts = [(1, ["C'est mon premier post", datetime(2020, 1, 1)]),
         (1, ["Flask est-il bien ?", datetime(2020, 1, 12)]),
         (1, ["Flask possède beaucoup d'extensions", datetime(2020, 1, 20)]),
         (2, ["C'est mon premier post", datetime(2020, 1, 4)]),
         (2, ["J'adore Symfony !", datetime(2020, 1, 10)]),
         (3, ["Mais Symfony est trop lourd...", datetime(2020, 1, 12)]),
         (3, ["Mais c'est plus simple à utiliser.", datetime(2020, 1, 16)]),
         (4, ["Symfony est comparable à Django.", datetime(2020, 1, 14)]),
         (4, ["Pas du tout", datetime(2020, 1, 18)])]
for u in users:
    user = User(username=u[0], email=u[1], about_me="Je parle de moi dans cette partie !")
    user.set_password("test")
    db.session.add(user)
    db.session.commit()
for p in posts:
    u = User.query.get(p[0])
    post = Post(body=p[1][0], author=u, timestamp=p[1][1])
    db.session.add(post)
    db.session.commit()
