class User:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        print(f"Creat Account, User name: {self.name}, Current Balance: {self.balance}")

    def make_deposit(self,amount):
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
        self.balance -= amount
        other_user.balance += amount
        print(f"Transfer: ${amount} from: {self.name}, to: {other_user.name}")
        return self

# add users
guido = User("Guido Van Rossum", 500)
Mahmoud = User("Mahmoud Shuman", 300)
Ahmad = User("Ahmad Ali")

guido.make_deposit(100).make_deposit(63.9).make_deposit(14.2).make_withdrawal(120.5).display_user_balance()

Mahmoud.make_deposit(665.3).make_deposit(246).make_withdrawal(665.3).make_withdrawal(96).display_user_balance()

Ahmad.make_deposit(532.4).make_withdrawal(24).make_withdrawal(98).make_withdrawal(75).display_user_balance()