#   Create expenses = [] and add_expense(expenses). The function
#   asks for description, amount and category, builds ONE
#   dictionary and adds it to the list.
#
# PROCESS:
#   1. expenses = [] is the WHOLE collection, created outside the
#      function.
#   2. add_expense(expenses) receives that list as a parameter.
#   3. Inside, we build ONE dictionary called `expense`.
#   4. expenses.append(expense) adds the new dictionary to the list.
#      Lists are changed in place, so the original list grows and
#      nothing needs to be returned.
#   5. We call the function twice, then print the list.


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


def add_expense(expenses):
    description = input("Description: ").strip()
    amount = get_positive_number()
    category = input("Category: ").strip().lower()

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
    }
    expenses.append(expense)


expenses = []

add_expense(expenses)
add_expense(expenses)

print(expenses)