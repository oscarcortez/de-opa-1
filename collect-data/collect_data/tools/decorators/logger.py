def logger(func):
    def wrapper(*args, **kwargs):
        print(func.__name__,': ',end="")
        try:
            print('Started', end="")
            result = func(*args, **kwargs)
        except Exception as e:
            print(f", Error in: {e}", end="")
            raise  # Re-lanza la última excepción
        else:
            print(f', Successful')
            return result
    return wrapper
