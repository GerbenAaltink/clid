from orm.utils.get_models import get_models


def get_by_uuid(uuid_value, field_name='uuid'):
    for model_object in get_models():

        if not hasattr(model_object, field_name):
            continue

        try:
            found = model_object.objects.get(**{field_name:uuid_value})
        except model_object.DoesNotExist:
            continue

        return found
