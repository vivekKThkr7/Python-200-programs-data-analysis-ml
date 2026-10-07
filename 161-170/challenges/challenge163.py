#   Create an add_expense() function. Ask for description, amount
#   and category, build ONE dictionary and return it.



def get_positive_number():
    while True:
        try:
            number = float(input("Enter amount: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if number > 0:
            if number.is_integer():
                number = int(number)
            return number

        print("Amount must be greater than 0.")


def add_expense():
    description = input("Description: ").strip()
    amount = get_positive_number()
    category = input("Category: ").strip().lower()

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
    }
    return expense


expense = add_expense()
print(expense)