#!/bin/bash
coverage run manage.py test cherrymusic.apps -v 2 && \
coveralls
