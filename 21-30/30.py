# Mini ATM Decision Program

balance = 50000

amount = float(input("Enter withdrawl amount: "))

if amount <= 0:
    print("Invalid amount")

elif amount > balance:
    print("insufficient balance")

else:
    balance = balance - amount
    print("Withdrawl successful")
    print("Remaining Balance", balance)

