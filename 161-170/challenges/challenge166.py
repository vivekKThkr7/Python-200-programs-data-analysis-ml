# Create find_by_category(expenses, category) that returns only that expenses matching the category.
# find_by_category(expenses, "food") -> the two food expenses.


def find_by_category(expenses, category):
    matches = []
    for expense in expenses:
        matches.append(expense)

    return matches

expenses = [
    {"description": "Lunch", "amount": 25, "category": "food"},
    {"description": "Taxi", "amount": 15, "category": "travel"},
    {"description": "Coffee", "amount": 10, "category": "food"}
]

food_expenses = find_by_category(expenses, "food")

for expense in food_expenses:
    print(f"{expense['description']} -> {expense['amount']}")