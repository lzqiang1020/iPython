class MyClass:
    """This is a class"""
    xxx = 'XXX'

    def foo(self):
        print("class-method: foo")

    def bar():
        print("bar")

    @classmethod
    def clsmtd(cls):
        print("{}.xxx={}".format(cls.__name__, cls.xxx))



a = MyClass()
a.foo()

# MyClass.bar()
# print(MyClass.__dict__)