class Atm:
    def __init__(self):
        self.balance = 100
        self.show_balance() # self keyword and it points to current object that is bank1

    def show_balance(self):
        print(self.balance)
    def __del__(self):
        print("Destructor called, object is being deleted")



bank1 = Atm() 