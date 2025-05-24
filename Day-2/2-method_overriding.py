class Animal:
    @staticmethod
    def speak():
        print("Animal speaks")

class Dog(Animal):
    @staticmethod
    def speak():
        print("Dog barks")

a1 = Animal()
a1.speak()
d1 = Dog()
d1.speak()