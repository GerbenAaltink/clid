import os
import sys

import django

from django.conf import settings
from django.core.management import call_command
from django.core.management.commands import test
from utils import *

if not settings.configured:

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings_test")

    django.setup()

    call_command('makemigrations', interactive=False)
    call_command('migrate', interactive=False)


test