class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showage(self):
        print('{} is {}'.format(self.name, self.age))

tom = Person('tom', 10)
jerry = Person('jerry', 40)

print()