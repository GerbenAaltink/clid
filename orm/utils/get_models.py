from orm.utils import DEFAULT_EXCLUDE_MODELS_FROM_MODULES, BaseModel


def is_excluded_module(model, exclude_modules=DEFAULT_EXCLUDE_MODELS_FROM_MODULES):

    for exclude_module in exclude_modules:
        if str(model.__module__).startswith(str(exclude_module)):
            return True

    return False


def get_models(exclude_modules=DEFAULT_EXCLUDE_MODELS_FROM_MODULES):

    model_list = []
    
    for model in BaseModel.__subclasses__():

        if exclude_modules and is_excluded_module(model=model, exclude_modules=exclude_modules):
            continue

        model_list.append(model)
        
    return model_list