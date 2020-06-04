class Person:
    """this is the class: Person"""

    def __init__(self, name, age=18):
        self.name = name
        self.__age = age

    def growup(self, inc=1):
        if 0 < inc < 150:
            self.__age += inc

    def getage(self):
        return self.__age

print(Person.__dict__, '\n')
tom = Person('tom')
print(tom.__dict__)