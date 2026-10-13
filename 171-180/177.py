# Testing with " assert "
# Testing checks whether your dode produces the results it is supposed to produce.


def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


assert calculate_total(10, 3) == 30
assert calculate_total(0, 5) == 0
assert calculate_total(2.5, 4) == 10.0

print("All tests passed!")


# Why test several examples?
# One successful example doesn't prove a function works in every situation.
# Our tests cover:
# Test	What it checks
# 10 × 3	Normal calculation
# 0 × 5	Zero-price edge case
# 2.5 × 4	Decimal calculation