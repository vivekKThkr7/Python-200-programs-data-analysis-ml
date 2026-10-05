# Calculator Total Expenses.

expenses = [
    {"description": "Lunch", "amount": 25.5},
    {"description": "Taxi", "amount": 15},
    {"description": "Coffee", "amount": 8}
]

total = 0

for expense in expenses:
    total += expense["amount"]

print("Total expenses:", total)