#!/bin/sh

cd ./backend
pipenv shell
celery --app=tasks.app worker