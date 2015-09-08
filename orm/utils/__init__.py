DEFAULT_EXCLUDE_MODELS_FROM_MODULES = [None, '__init__', 'django']

import django.db.models as django_models

BaseModel = django_models.Model
from get_models import get_models
from get_by_uuid import get_by_uuid


