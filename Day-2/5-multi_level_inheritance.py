class base:
    def dance(self):
        print("Dance")

class derived1(base):
    pass 

class derived2(derived1):
    pass 

d1 = derived2()

d1.dance()

