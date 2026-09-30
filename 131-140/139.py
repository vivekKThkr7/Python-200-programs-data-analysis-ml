# return from a method

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

account = BankAccount(5000)

balance = account.check_balance()

print("Balance: ", balance)
