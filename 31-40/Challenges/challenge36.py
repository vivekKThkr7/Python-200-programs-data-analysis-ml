balance = 100000

print("__________ATM Withdrawl System____________")
print("1. Balance Enqury")
option =int(input("Choose an option: "))

if option == 1:
    print("Current balance:", balance)
elif option == 2:
    withdrawl_amount = int(input("Enter amount to withdrawl: "))
    if withdrawl_amount<= balance and withdrawl_amount % 100 == 0:
        print("withdrawl Successful")
    else:
        print("Insufficient balance")

else:
    print("...........")
    