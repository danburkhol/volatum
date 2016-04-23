#!/bin/bash
DB_NAME=test
createdb $DB_NAME
python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('carlos', 'carlosyells@yahoo.com', 'carlos')" | ./manage.py shell

