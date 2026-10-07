#   Build a small Expense Tracker with a menu:
#       1. Add Expense   2. View Expenses   3. Report   4. Exit
#   Functions: add_expense(), show_expenses(), show_report().
#   Allowed: functions, list, dictionaries, loops, conditions,
#   try/except. Not allowed: classes, external libraries, JSON.
#
# PROCESS:
#   1. expenses = [] holds every record (whole collection).
#   2. get_positive_number() safely reads an amount (from 161).
#   3. add_expense(expenses) builds ONE dictionary (163/169) and
#      appends it to the list.
#   4. show_expenses(expenses) loops through the list and prints
#      one line per expense (164/168). If the list is empty it
#      says so.
#   5. show_report(expenses) calculates the total (165), the count
#      with len(), and the average = total / count. An empty list
#      is checked first to avoid dividing by zero.
#   6. main() runs a `while True` menu loop; choices 1-3 call the
#      functions, 4 uses `break` to stop, anything else shows an
#      error message.



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
    print("Expense added.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    for expense in expenses:
        print(f"{expense['description']} - {expense['amount']} - {expense['category']}")


def show_report(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    total = 0
    for expense in expenses:
        total += expense["amount"]

    count = len(expenses)
    average = total / count

    print("Total expenses:", total)
    print("Number of expenses:", count)
    print(f"Average expense: {average:.2f}")


def show_menu():
    print("\n----- Expense Tracker -----\n")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Report")
    print("4. Exit")


def main():
    expenses = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_report(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


main()