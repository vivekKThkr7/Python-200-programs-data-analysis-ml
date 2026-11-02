# Mini ATM Decision Program

balance = 100000
print("______ATM______")
print("1. Balance enquiry")
print("2. Cash withdrawal")
print("3. Balance deposit")

option = int(input("Enter an option: "))

if option == 1:
    print("Current available amount:", balance)
elif option == 2:
    withdrawal_amount = float(input("Enter withdrawal amount: "))

    if withdrawal_amount <= 0:
        print("Invalid amount. Enter an amount greater than zero.")
    elif withdrawal_amount > balance:
        print("Insufficient balance")
    else:
        balance -= withdrawal_amount
        print("Cash withdrawal:", withdrawal_amount)
        print("Amount remaining in account:", balance)
elif option == 3:
    deposit_amount = float(input("Enter amount to deposit: "))

    if deposit_amount <= 0:
        print("Invalid amount. Enter an amount greater than zero.")
    else:
        balance += deposit_amount
        print("Available amount:", balance)
else:
    print("Invalid option. Please choose 1, 2, or 3.")
