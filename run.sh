#!/bin/sh
export FLASK_APP=./scheduler/app.py

pipenv run flask run -h 0.0.0.0 -p 8000 --debug
