class Person:
    name = "nobody"
    @classmethod
    def changeName(cls,name):
        cls.name = name

ob1 = Person()

print(ob1.name)
ob1.changeName("somebody")
print(ob1.name)
print(Person.name)