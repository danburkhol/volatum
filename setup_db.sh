#!/bin/bash
python manage.py syncdb --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('carlos', 'carlos.ferreira@us.ibm.com', 'carlos')" | python manage.py shell

