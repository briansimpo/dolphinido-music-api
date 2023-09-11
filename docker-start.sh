#!/usr/bin/env bash

set -e
 
role=${CONTAINER_ROLE:-app}

if [ "$role" == "app" ]; then
    gunicorn wsgi:application --bind 0.0.0.0:8000 
	   
elif [ "$role" == "queue" ]; then
    python craft queue:work
fi

exec "$@"