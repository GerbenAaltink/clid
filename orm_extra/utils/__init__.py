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

DEFAULT_EXCLUDE_MODELS_FROM_MODULES = (None, 'django', '__init__')
from get_models import get_models
from get_by_uuid import get_by_uuid