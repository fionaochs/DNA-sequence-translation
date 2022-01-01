#!/bin/sh

cd ./backend
pipenv shell
celery -A sequences_api  worker -l info