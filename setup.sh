#!/bin/sh

# source .venv/bin/activate
pipenv shell
python ./manage.py runserver

cd ./frontend
npm start