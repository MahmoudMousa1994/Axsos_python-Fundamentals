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
    
    def user_deposit(self,amount):
        print(f"User {self.name} made a Deposit With: ${amount}")
        self.account.deposit(amount)
        return self
    
    def user_withdraw(self,amount):
        print(f"User {self.name} made a Withdrow With: ${amount}")
        self.account.withdraw(amount)
        return self
    

    def user_info(self):
        print(f"Name: {self.name}")
        print(f"email: {self.email}")
        self.account.display_account_info()
        return self


Mahmoud = User("Mahmoud Shuman", "mahmoud.shuman@outlook.com")
Ahmad = User("Ahmad Ali","ahmad.ali@outlook.com")


Mahmoud.user_deposit(1000).user_deposit(999).user_deposit(500).user_info().user_withdraw(300).user_withdraw(200).user_withdraw(4000).user_info()
print("-_*"*30)
Ahmad.user_deposit(2000).user_deposit(1000).user_deposit(500).user_info().user_withdraw(4000).user_info()
