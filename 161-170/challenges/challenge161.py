# Challenge161 - Safe Positive Number
# Create get_positive_number(). It should asking the user for a number until a valid one is entered.
# - Positive nyumber -> return it
# - 0 or negative -> ask again
# - Text -> don't crash, ask again

def get_positive_number():
    while True:
        try:
            number = float(input("Enter amount: "))

        except ValueError:
            print("Please enter a valid number. ")
            continue

        if number > 0: 
            if number.is_integer():  # show 150 instead of 150.0
                number = int(number)
            return number


        print("Amount must be greater that 0.")

amount = get_positive_number()
print("Amount: ", amount)

