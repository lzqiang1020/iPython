# def copy_properties(src, dst):
#     dst.__name__ = src.__name__
#     dst.__doc__ = src.__doc__

def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst
    return _copy

def logger(fn):
    @copy_properties(fn)                  # wrapper = copy_properties(fn)(wrapper) = _copy(wrapper)
    def wrapper(*args, **kwargs):
        '''I'm wrapper'''
        print('begin')
        x = fn(*args, **kwargs)
        print('end')
        return x
    # copy_properties(fn, wrapper)
    return wrapper

@logger
def add(x, y):
    """This is a function for add"""
    return x + y

print("name={}, doc={}".format(add.__name__, add.__doc__))