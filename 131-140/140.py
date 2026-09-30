# Mini bank Account Object
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def check_balance(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            print("Deposit successful")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            print("Withdrawal successful")


account = BankAccount("Vivek", 5000)

account.check_balance()

account.deposit(1000)

account.withdraw(2000)

account.check_balance()