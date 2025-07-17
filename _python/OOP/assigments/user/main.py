class User:
    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
        print(f"Creat Account, User name: {self.name} Current Balance: {self.balance}")

    def make_deposit(self,amount):
        self.balance += amount
        print(f"User {self.name} made a Deposit with {amount}")
    
    def make_withdrawal(self,amount):
        self.balance -=amount
        print(f"User {self.name} made a Withdrawal with {amount}")

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance += amount
        print(f"Transfer: ${amount} from: {self.name}, to: {other_user.name}")


# add users
guido = User("Guido Van Rossum", 500)
Mahmoud = User("Mahmoud Shuman", 300)
Ahmad = User("Ahmad Ali")

# invoke  methods (Deposit) for guido 
guido.make_deposit(100)
guido.make_deposit(63.9)
guido.make_deposit(14.2)
# invoke  methods (Withdrawal) for guido 
guido.make_withdrawal(120.5)
# invoke (display user info) method  for guido 
guido.display_user_balance()

# --------------------------------------------

# invoke  methods (Deposit) for Mahmoud 
Mahmoud.make_deposit(665.3)
Mahmoud.make_deposit(246)
# invoke  methods (Withdrawal) for Mahmoud
Mahmoud.make_withdrawal(665.3)
Mahmoud.make_withdrawal(96)
# invoke (display user info) method  for Mahmoud
Mahmoud.display_user_balance()

# --------------------------------------------

# invoke  methods (Deposit) for Ahmad
Ahmad.make_deposit(532.4)
# invoke  methods (Withdrawal) for Ahmad
Ahmad.make_withdrawal(24)
Ahmad.make_withdrawal(98)
Ahmad.make_withdrawal(75)
# invoke (display user info) method for Ahmad
Ahmad.display_user_balance()


# before transfer
guido.display_user_balance()
Ahmad.display_user_balance()
# invoke Bonus (Transfer)
guido.transfer_money(Ahmad, 200)
# after transfer
guido.display_user_balance()
Ahmad.display_user_balance()
