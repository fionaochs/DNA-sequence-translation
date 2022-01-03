#!/bin/sh
#!/usr/bin/python
#!/usr/local/bin/celery

cd ./backend
pipenv shell
celery -A sequences_api  worker -l info