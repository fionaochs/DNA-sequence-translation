#!/bin/sh

# source .venv/bin/activate
cd ./backend
pipenv shell
pip install -r requirements.txt
python ./manage.py runserver;

