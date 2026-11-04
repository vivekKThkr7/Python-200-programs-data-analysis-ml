#   Read outputs/json/expenses.json with json.load(), then loop through the
#   loaded data and display each expense.
#   (Run challenge167.py first so the file exists.)


import json

try:
    with open("outputs/json/expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    print("outputs/json/expenses.json not found. Run challenge167.py first.")
    expenses = []

for expense in expenses:
    print(f"{expense['description']} - {expense['amount']} - {expense['category']}")