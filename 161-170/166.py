# Filter expenses by Category
# Suppose we want only food expenses.
expenses = [
    {"description": "Lunch", "amount": 25.5, "category": "Food"},
    {"description":"Taxt", "amount": 15, "category": "Travel"},
    {"description": "Coffee", "amount": 8, "category": "Food"}
]

for expense in expenses:
    if expense ["category"] == "Food":
        print(
            expense["description"],
            "->",
            expense["amount"]
        )