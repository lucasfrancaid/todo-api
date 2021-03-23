#!/bin/bash

./manage.py makemigrations --noinput
./manage.py migrate
./manage.py create_admin

exec "$@"