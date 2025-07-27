class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def withdrow(self, amount):
        if (self.balance - amount)>0:
            self.balance-= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)
        self.is_roth= is_roth

    def withdrow(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdrow(amount)
        return self


Mahmoud = RetirementAccount(0.03,is_roth=True, balance=1000)
Mahmoud.withdrow(100, is_early=False)
print(Mahmoud.balance)
