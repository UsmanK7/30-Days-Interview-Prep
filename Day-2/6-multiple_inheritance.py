class A:
    def printer(self):
        print("A")
class B:
    def printer(self):
        print("B")

class C(A,B):
    pass 

c = C()
c.printer()
