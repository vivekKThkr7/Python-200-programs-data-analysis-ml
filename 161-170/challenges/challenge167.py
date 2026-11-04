#   Save a list of expenses to outputs/json/expenses.json using json.dump(),
#   so the data is still there after the program finishes.
#

import json

expenses = [
    {"description": "Lunch", "amount": 25, "category": "food"},
    {"description": "Taxi", "amount": 15, "category": "travel"},
]

with open("outputs/json/expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)

print("Expenses saved to outputs/json/expenses.json")