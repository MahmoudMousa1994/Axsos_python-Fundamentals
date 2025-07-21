class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"new user name:{name} user balance: {balance}")

    def make_deposit(self, amount):
        self.balance += amount
        print(f"User {self.name} made a Deposit with {amount}")
        return self

    def make_withdrawal(self,amount):
        self.balance -=amount
        print(f"User {self.name} made a Withdrawal with {amount}")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print(f"Transfer: ${amount} from: {self.name}, to: {other_user.name}")
        return self
Guido = User("Guido Van Rossum")
Guido.make_deposit(100)

Bashar = User("Bashhar", 500)
Bashar.make_deposit(600).make_deposit(600).make_deposit(600).make_deposit(600).make_withdrawal(300).make_withdrawal(300).transfer_money(Guido,400).display_user_balance()

# Bashar.make_withdrawal(300)
# Bashar.display_user_balance()

# Bashar.transfer_money(Guido,400)