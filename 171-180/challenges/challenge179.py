# Refactor the Receipt Program

# The following program works, but it repeats the same calculation and printing logic:

# item = "Keyboard"
# price = 25
# quantity = 3

# total = price * quantity

# print("Item:", item)
# print("Quantity:", quantity)
# print("Total:", total)

# item = "Mouse"
# price = 15
# quantity = 2

# total = price * quantity

# print("Item:", item)
# print("Quantity:", quantity)
# print("Total:", total)

# Improve the program by creating two functions: calculate_total(price, quantity) , display_receipt(item, quantity, total)

# Requirements
# - Move the calculation into calculate_total().
# - Move the receipt display into display_receipt().
# - Display receipts for both products.
# - Keep the results the same as the original program.
# - Avoid duplicating the calculation logic.


def calculate_total(price, quantity):
    return price * quantity


def display_receipt(item, quantity, total):
    print("Item:", item)
    print("Quantity:", quantity)
    print("Total:", total)


purchases = [
    ("Keyboard", 25, 3),
    ("Mouse", 15, 2),
]

for index, (item, price, quantity) in enumerate(purchases):
    if index > 0:
        print()
    display_receipt(item, quantity, calculate_total(price, quantity))