# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseModel',
            fields=[
                ('uuid', models.UUIDField(serialize=False, primary_key=True)),
            ],
        ),
    ]
