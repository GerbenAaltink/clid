DEFAULT_EXCLUDE_MODELS_FROM_MODULES = [None, '__init__']


class BaseModel(object):
    pass


class DoesNotExistException(Exception):
    pass


try:
    import django.db.models as django_models
except ImportError:
    pass
else:
    BaseModel = django_models.Model
    DEFAULT_EXCLUDE_MODELS_FROM_MODULES.append('django')

from get_models import get_models
from get_by_uuid import get_by_uuid