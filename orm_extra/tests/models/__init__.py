from django.db.models import UUIDField
from orm_extra.utils import BaseModel

from django.conf import settings as django_settings

if not django_settings.configured:
    django_settings.configure()


class TestCaseModel(BaseModel):

    pk = UUIDField(primary_key=True)

    class Meta:
        app_label = 'test-model'