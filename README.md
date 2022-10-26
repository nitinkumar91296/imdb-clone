# imdb-clone
IMDB-clone is a Python Django-Rest-Framework based microservice.


extensions: python, python extension pack, tabnine

STEPS:
activate venv (python -m venv venv -> source venv/bin/activate)
pip install Django==4.1.1
django-admin startproject imdb
cd imdb
python manage.py makemigrations
python manage.py migrate
python manage.py startapp imdb_app
