import os
import sys
from django.core.management.commands import test
from utils import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings_test")

import django

django.setup()

from django.core.management import call_command

#call_command('schemamigration', 'orm')

call_command('makemigrations', 'orm',initial=True,interactive=False)
call_command('migrate', 'orm',interactive=False)
