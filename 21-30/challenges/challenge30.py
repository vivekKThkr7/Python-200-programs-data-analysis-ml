# print("Choose an Option")
# print("1. Check balance")
# print("2. Withdraw")
# print("3. Deposit")
# option = int(input("Select option number: "))

# if option == 1:
#     print("Check balance")

# elif option == 2:
#     print("Withdraw")

# elif option == 3:
#     print("Deposit")


balance = 50000

print("____ATM____")
print("1. Check Balance")
print("2. Withdraw")
print("3. Deposit")

option = int(input("Select an option: "))

if option == 1:
    print("Your balance is ", balance)

elif option == 2:
    withdrawal_amount = float(input("Enter amount to withdraw: "))

    if withdrawal_amount<=0:
        print("Invalid amount")

    elif withdrawal_amount > balance:
        print("insufficient balance")

    else:
        balance = balance-withdrawal_amount
        print("Withdrawl successful")
        print("Remaning balance: ", balance)

elif option == 3:
    depost_amount =float(input("Enter depost amount: "))

    if depost_amount <=0:
        print("invalid")

    else:
        balance = balance+depost_amount
        print("Depost Successful")
        print("New balance: ", balance)

else:
    print("Invalid option")

