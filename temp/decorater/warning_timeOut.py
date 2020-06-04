import time
import datetime

def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst
    return _copy

def logger(duration):
    def _logger(fn):
        @copy_properties(fn)
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            print("So slow.") if delta > duration else print("So fast.")
            return ret
        return wrapper
    return _logger

@logger(2)
def add(x, y):
    print("Function is called, begin")
    time.sleep(3)
    return x + y

print(add(3, 10), add.__name__, add.__doc__, add.__qualname__, sep='\n')
