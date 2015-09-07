from orm_extra.utils import DEFAULT_EXCLUDE_MODELS_FROM_MODULES, BaseModel


def get_models(exclude_modules=DEFAULT_EXCLUDE_MODELS_FROM_MODULES):
    
    model_list = []
    
    for model in BaseModel.__subclasses__():

        if exclude_modules:

            module = str(model.__module__).split('.').pop()

            if module in exclude_modules:
                continue
            
        model_list.append(model)
        
    return model_list