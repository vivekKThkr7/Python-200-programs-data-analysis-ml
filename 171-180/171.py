# Safe Positive amount. 
# Create a reusable function.

def get_positive_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

amount = get_positive_amount()

print("Amount:", amount)