# Validate Positive Numbers
# Validation means checking whether input is acceptable before using it.

def get_positive_number():
    while True:
        try:
            number = float(input("Enter an amount: "))

            if number > 0:
                return number

            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


amount = get_positive_number()
print("Amount: ", amount)



# Here instead of trusting the user: "please type correctly"
# we make the program protect itself.

