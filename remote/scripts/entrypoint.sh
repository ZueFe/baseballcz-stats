#!/bin/sh

pipenv run pip install -r requirements.txt && \
pipenv run xvfb-run python app.py