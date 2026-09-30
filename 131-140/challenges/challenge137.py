# Create 
# class bankAccount:
# with
# balance
# deposit()
# deposit() should increase the balance.

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount(1000)

print("Before deposit:", account.balance)

account.deposit(500)

print("After deposit:", account.balance)
