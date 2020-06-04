
# def setnameproperty(cls, name):
#     cls.name = name

def setnameproperty(name):
    def wrapper(cls):
        cls.name = name
        return cls
    return wrapper


@setnameproperty('my class')
class MyClass:
    pass

print()