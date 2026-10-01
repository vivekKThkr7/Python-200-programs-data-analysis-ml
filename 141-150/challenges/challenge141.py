# Create a " bankAccount " class with a private.
# __balance  and a method " get_balance() "

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)

print(account.get_balance())

        