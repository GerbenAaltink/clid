from django.conf import settings as django_settings
from django.db.models import UUIDField, Model


class TestCaseModel(Model):

    uuid = UUIDField(primary_key=True)

    class Meta:
        app_label = 'orm_tests'