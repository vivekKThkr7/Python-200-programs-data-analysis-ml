# Method with a Condition

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount!!")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            print("Withdrawal Successful")

account = BankAccount(5000)
account.withdraw(1000)
print("Balance: ", account.balance)

