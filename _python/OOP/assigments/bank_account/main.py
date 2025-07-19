class BankAccount:
    def __init__(self, int_rate= 0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance +=amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return self
        else:
            print("Insufficint funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance >0 :
            self.balance +=self.balance * self.int_rate
            return self
            

guido = BankAccount(0.03 , 300)
Mahmoud = BankAccount(0.025,600)

guido.display_account_info().deposit(42).deposit(7).deposit(3.9).display_account_info().withdraw(90).display_account_info().yield_interest().display_account_info()
Mahmoud.display_account_info().deposit(200).deposit(500).display_account_info().withdraw(300).withdraw(300).withdraw(300).withdraw(450).display_account_info().yield_interest().display_account_info()





