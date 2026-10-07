#   Create display_expense(expense) that shows one expense as:
#       Lunch -> 25 -> food


def display_expense(expense):
    print(f"{expense['description']} → {expense['amount']} → {expense['category']}")


expense = {
    "description": "Lunch",
    "amount": 25,
    "category": "food",
}

display_expense(expense)