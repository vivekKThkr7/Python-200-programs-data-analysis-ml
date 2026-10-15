# Type-hinted Calculator
# Write a function named: " calculate_total(price, quantity) " 
# requirements.
# 1. Add suitable type to both parameters.
# 2. Add a return type hint
# 3. Return ht calcualted total.
# 4. Display the results clearly.

# Extra task ⭐
# Create another function:  " calculate_average(numbers) "

# It must accept a list of numbers and return their average.
# Handle an empty list sensibly so that your function does not attempt to divide by zero.
# Checkpoint: Type hints explain the intended types; they do not automatically validate every input at runtime.

def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0  # avoid dividing by zero
    return sum(numbers) / len(numbers)


tests = [(10, 3), (40, 3), (0, 5)]

print(f"{'Price':<8}{'Quantity':<10}{'Total':<8}")
for price, quantity in tests:
    print(f"{price:<8}{quantity:<10}{calculate_total(price, quantity):<8}")

print()
print("Average of [10, 20, 30]:", calculate_average([10, 20, 30]))
print("Average of []:", calculate_average([]))

