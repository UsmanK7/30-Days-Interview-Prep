class A:
    def dance(self):
        print("dance")

class B(A):
    pass

obj = B()
obj.dance()