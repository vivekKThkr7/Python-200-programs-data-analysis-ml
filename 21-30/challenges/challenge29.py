balance = int(input("Enter an amount: "))
withdrawl_amount = int(input("Enter amount to withdraw: "))

if withdrawl_amount <= 0:
    print("Invalid amount")

elif withdrawl_amount > balance:
    print("Insufficient balance")

else: 
    print("withdrawal successful")
    

