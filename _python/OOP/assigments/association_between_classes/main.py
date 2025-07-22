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



class User:
    def __init__(self, name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate= 0.02, balance=0)

    def user_info(self):
        print(f"Name: {self.name}")
        print(f"email: {self.email}")
        self.account.display_account_info()
        return self


Mahmoud = User("Mahmoud Shuman", "mahmoud.shuman@outlook.com")

Mahmoud.account.deposit(100).deposit(500).withdraw(650)
Mahmoud.user_info()