class Person:
    def normal_method():
        print("normal")

    def method(self):
        print("{}'s method".format(self))

    @classmethod
    def class_method(cls):
        print("class={0.__name__}({0})".format(cls))
        cls.HEIGHT = 170

    @staticmethod
    def static_method():
        print(Person.HEIGHT)

print('=====类访问')
print(1, Person.normal_method(),'\n')   # normal
# print(2, Person.method())   # error
print(3, Person.class_method(),'\n')   # class=Person
print(4, Person.static_method(),'\n')   #
print(Person.__dict__)

print("=====实例访问")
print("tom >>>>>")
tom = Person()
# print(1, tom.normal_method())   # error
print(2, tom.method())   # tom's method
print(3, tom.class_method())   #
print(4, tom.static_method())

print("jerry>>>>")
jerry = Person()
print(1, jerry.normal_method())
print(2, jerry.method())
print(3, jerry.class_method())
print(4, jerry.static_method())