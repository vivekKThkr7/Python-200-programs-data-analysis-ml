# Add. withdraw(), 
# Rules: 
# amount <= 0 → Invalid
# amount > balance → Insufficient balance
# otherwise → withdraw


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Withdrawal successful")


account = BankAccount(5000)

# Invalid amount
account.withdraw(0)
print("Balance:", account.balance)

# More than balance
account.withdraw(6000)
print("Balance:", account.balance)

# Valid withdrawal
account.withdraw(1000)
print("Balance:", account.balance)
