#  test your Function
# Write the following calculation function:
# def calculate_total(price, quantity):
#     return price * quantity

# Now test the function using assert.
# Your tests must verify : 10 × 3 = 30, 5 × 0 = 0, 2.5 × 4 = 10.0

# Requirements
# 1. Write an assertion for each calculation.
# 2. Compare the actual function result with the expected result.
# 3. Print All tests passed! only after all assertions have succeeded.


# Do not simply print the expected answers. Your tests must check the real function.
# Extra task ⭐
# Add another test for a calculation of your choice.

def calculate_total(price, quantity):
    return price * quantity


assert calculate_total(10, 3) == 30
assert calculate_total(5, 0) == 0
assert calculate_total(2.5, 4) == 10.0
assert calculate_total(7, 6) == 42  # extra test

print("All tests passed!")