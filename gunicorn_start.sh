#!/bin/bash

TOPLEVEL=~/ihstattler.com/
NAME="ihstattler"
DJANGODIR=$TOPLEVEL/$NAME
SOCKFILE=$TOPLEVEL/run/gunicorn.sock
USER=ubuntu
GROUP=ubuntu
NUM_WORKERS=8
DJANGO_SETTINGS_MODULE=ihstattler.settings
DJANGO_WSGI_MODULE=ihstattler.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source $TOPLEVEL/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $TOPLEVEL/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE
