# MINI EXPENSE TRACKER


import json

def load_expenses():
    try:
        with open("outputs/json/expenses.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open("outputs/json/expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def view_expenses(expenses):

    if len(expenses) == 0:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        print(
            expense["description"],
            "-",
            expense["amount"],
            "-",
            expense["category"]
        )

        total += expense["amount"]

    print("Total expenses:", total)


expenses = load_expenses()

while True:

    print()
    print("----- Expense Tracker -----")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")