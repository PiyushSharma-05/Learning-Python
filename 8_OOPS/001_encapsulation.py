class BankAccount:
    def __init__(self, name, balance):
        self.name = name #public
        self.__balance = balance #private 

    def get_balance(self): #getter
        return self.__balance
    
    def set_balance(self, new_balance): #setter
        self.__balance = new_balance 
    
acc1 = BankAccount("Piyush", 99_999)

acc1.set_balance(100000)
print(acc1.name, acc1.get_balance())