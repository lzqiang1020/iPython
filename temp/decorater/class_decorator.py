class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print("class decorator running.")
        self._func()
        print("class decorator ending.")

@Foo
def bar():
    print("I'm bar.")

print(bar)
# bar = Foo(bar)
# bar.__call__()