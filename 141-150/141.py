# Encapsulation : Keeping an object's data and the methds that control
#  that data together, while limiting direct access when needed.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print(account.get_balance())


# The double underscore indicates that we're making this attribute more restricted from direct outside access.
        


