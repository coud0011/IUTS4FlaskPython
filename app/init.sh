#!/bin/bash
if [ -e /working ]
then
  # shellcheck disable=SC2164
  cd /working/coud0011/archilogiciel/flask/
else
  echo "Implémenter ce qu'il faut à la place de ce message pour insérer votre path personnel."
fi
source env_flask/bin/activate
if ! [ -e app/app.db ]
then
    flask db upgrade
fi
python3 app/requetes.py
flask shell
