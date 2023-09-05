from loaders import SpinningLoader
loader = SpinningLoader()

def console_loader(func):    
    def wrapper(*args, **kwargs):
        
        try:
            print('Step:',func.__name__)
            loader.start()
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Error in: {e}")
            raise  
        else:
            loader.stop()
            return result
    return wrapper

