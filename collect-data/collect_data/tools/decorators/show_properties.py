def show_properties(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        properties = vars(instance)
        print(f"Class {cls.__name__}:")
        for key, value in properties.items():
            print(f"\t{key}: {value}")
        return instance
    return wrapper