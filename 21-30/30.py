# Mini ATM Decision Program

# balance = 50000

# amount = float(input("Enter withdrawl amount: "))

# if amount <= 0:
#     print("Invalid amount")

# elif amount > balance:
#     print("insufficient balance")

# else:
#     balance = balance - amount
#     print("Withdrawl successful")
#     print("Remaining Balance", balance)


balance = 100000
print("______ATM______")
print("1. balance enqury")
print("2. Cash Withdrawl")
print("3. Balance Deposit")

option = int(input("Enter any number: "))
if option == 1:
    print("Current available amount: ", balance)

elif option == 2:
    withdrawl_amount = float(input(" Enter withdrawl amount: "))

    if withdrawl_amount> balance:
        print("Insufficient balance")

    elif withdrawl_amount <= balance:
        print("Cash withdrawl: ", withdrawl_amount)
        remaining_balance = balance- withdrawl_amount
        print("Amount remaining in account: ", remaining_balance)

    else:
        print("invalid Input")

elif option ==3:
    deposit_balance = float(input("Enter amount to deposit: "))

    balance += deposit_balance
    print("Available amount: ", balance)