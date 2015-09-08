from django.core.exceptions import FieldError
from orm.utils.get_models import get_models


def get_by_uuid(uuid_value, field_name='uuid'):

    uuid_string = str(uuid_value)

    for model_object in get_models():
        try:
            return model_object.objects.get(**{field_name:uuid_string})
        except model_object.DoesNotExist:
            pass
        except FieldError:
            pass