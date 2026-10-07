# Given a list of expense dictionaries, create calculate_total(expenes) and show: Total; 48


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    return total


expenses = [
    {"description": "Lunch", "amount": 25},
    {"description": "Taxi", "amount": 15},
    {"desciption": "Coffee", "amount": 10}
]


print("Total: ", calculate_total(expenses))