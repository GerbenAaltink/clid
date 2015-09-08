from django.conf import settings as django_settings
from django.db import models


class TestCaseModel(models.Model):

    uuid = models.UUIDField(primary_key=True)

    class Meta:
        app_label = 'orm'