#!/bin/sh
export FLASK_APP=flaskblog.py
export FLASK_DEBUG=1
flask run -h 0.0.0.0
