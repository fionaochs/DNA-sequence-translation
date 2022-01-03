#!/bin/sh

cd ../backend
# source .venv/bin/activate
pipenv shell
# pip install -r requirements.txt
python manage.py runserver;
