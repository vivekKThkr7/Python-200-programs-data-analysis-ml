balance = 100000

print("----- ATM -----")
print("1. Balance Inquiry")
print("2. Withdraw")

option = int(input("Choose an option: "))

if option == 1:
    print("Current balance:", balance)

elif option == 2:
    withdrawal_amount = int(input("Enter amount to withdraw: "))

    if withdrawal_amount <= 0:
        print("Invalid amount")

    elif withdrawal_amount > balance:
        print("Insufficient balance")

    elif withdrawal_amount % 100 != 0:
        print("Amount must be a multiple of 100")

    else:
        balance = balance - withdrawal_amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)

else:
    print("Invalid option")