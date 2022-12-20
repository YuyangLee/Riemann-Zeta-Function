from time import time
from functools import wraps

def timing(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time()
        result = function(*args, **kwargs)
        t1 = time()
        return result, (t1 - t0) * 1000
    return function_timer
