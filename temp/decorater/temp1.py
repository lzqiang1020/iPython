# def add_name(name, clz):
#     clz.NAME = name

def add_name(name):
    def wrapper(clz):
        clz.NAME = name
        return clz
    return wrapper

@add_name    #Person = add_name()
class Person:
    AGE = 3