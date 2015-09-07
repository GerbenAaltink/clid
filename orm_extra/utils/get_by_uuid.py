from orm_extra.utils.get_models import get_models


def get_by_uuid(uuid_value, field_name='pk'):
    for model_object in get_models():

        if not hasattr(model_object, field_name):
            continue

        try:
            model_object.objects.get(**{field_name:uuid_value})
        except model_object.DoesNotExist:
            continue

        return model_object