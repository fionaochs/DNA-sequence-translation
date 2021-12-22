#!/bin/sh

# source .venv/bin/activate
pipenv shell
python ./backend/manage.py runserver

cd ./frontend
npm start