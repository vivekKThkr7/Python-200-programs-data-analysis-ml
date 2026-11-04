# Load JSON data

import json

with open ("outputs/json/expenses.json", "r") as file:
    expenses = json.load(file)

for expense in expenses:
    print(expense)


# Program can save data and later restore it. 