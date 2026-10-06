# Add an expense using a Function

expenses = []

def add_expenses():
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully.")

add_expenses()

print(expenses)
