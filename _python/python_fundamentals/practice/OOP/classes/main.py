class user:
    pass
mhd = user()
mj=user()


#  attributes
class user:
    def __init__(self):
        self.name= "Mahmoud"
        self.email = "mahmoud.shuman@outlookcom"
        self.account_balance = 5


guido = user()
monty = user()
guido.name = "Guido"
monty.name = "Monty"
print(guido.name)
print(monty.name)

# methods
class user:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount


guido = user("Guido Van Rossum", "guido@python.com")
monty = user("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)
print(monty.account_balance)


