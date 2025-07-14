# class user:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(int_rate=0.02, balance=0)

# class User:
#     def example_method(self):
#         self.account.deposit(100)          
#         print(self.account.balance) 


class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def example_method(self):
        self.account.deposit(100)
        print(self.account.balance)



mhd = User("Mahmoud", "mahmoud@example.com")
mhd.example_method()  
