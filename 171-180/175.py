# Type Hints
# Type hints show what kinds of values a function expects and what it should return.


def calculate_total(price: float, quantity:int) -> float:
    return price * quantity

total = calculate_total(25.5, 3)

print("Total: ", total)
