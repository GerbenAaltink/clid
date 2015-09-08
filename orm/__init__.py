import os
import sys
import django
from django.core.management import call_command

from utils import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings_test")

django.setup()


#call_command('makemigrations', 'orm', interactive=False)
#call_command('migrate', 'orm', interactive=False)
call_command('syncdb',interactive=False)
