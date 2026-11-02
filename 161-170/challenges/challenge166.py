# Return only the expenses whose category matches the requested category.

def find_by_category(expenses, category):
    matches = []
    category = category.strip().lower()

    for expense in expenses:
        expense_category = expense.get("category", "").strip().lower()
        if expense_category == category:
            matches.append(expense)

    return matches


expenses = [
    {"description": "Lunch", "amount": 25, "category": "food"},
    {"description": "Taxi", "amount": 15, "category": "travel"},
    {"description": "Coffee", "amount": 10, "category": "food"},
]

food_expenses = find_by_category(expenses, "food")

for expense in food_expenses:
    print(f"{expense['description']} -> {expense['amount']}")
