#!/bin/sh

# source .venv/bin/activate
cd ./backend
pipenv shell
python ./manage.py runserver;
