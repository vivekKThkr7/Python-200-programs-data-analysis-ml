# Challenge 141
# Create a BankAccount class with a private __balance
# and a get_balance() method.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)
print("Balance:", account.get_balance())
