#!/bin/sh

# source .venv/bin/activate
cd ./backend
pipenv shell
# pip install -r requirements.txt
python ./manage.py runserver;

pipenv shell
celery -A sequences_api  worker -l info;

cd ../frontend
npm run start-react;