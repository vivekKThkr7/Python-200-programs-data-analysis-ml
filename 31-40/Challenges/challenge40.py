print("______Mini Bank System______")
print("1. Check Balance")
print("2. Withdraw")
print("3. Deposit")
print("4. Loan Eligibility")

option = int(input("Choose an option: "))

balance = 100000

if option == 1:
    print("Current balance = ", balance)
elif option == 2:
    withdrawl_amount = float(input("Enter the withdrawl amount: "))
    if withdrawl_amount <= balance:
        if withdrawl_amount % 100 == 0:
            print("Withdrawl successful")
            balance = balance - withdrawl_amount
            print("Current balance in account : ", balance)
        else:
            print("Enter the amount in the multiple of 100.")
    else:
        print("No ehough balance")
elif option == 3:
    deposit = float(input("Enter deposit amount: "))
    balance += deposit
    print(deposit," has been deposited")
    print("Avaiable amount in account: ", balance)
elif option == 4:
    age = int(input("Enter your age: "))
    monthly_income = float(input("Enter your monthly income: "))
    is_employeed = input("Are you employed or have own business: ")
    
    if age >=18 and monthly_income >=50000 and is_employeed == "yes":
        print("you are eligible to get loan")
    else:
        print("You are not eligible.")