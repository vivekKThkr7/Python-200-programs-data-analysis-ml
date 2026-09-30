# Method that changes data

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount(1000)

print("Before:", account.balance)

account.deposit(500)

print("After:", account.balance)