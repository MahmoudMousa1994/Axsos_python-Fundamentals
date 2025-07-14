class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

class User:
    def example_method(self):
        self.account.deposit(100)          
        print(self.account.balance) 