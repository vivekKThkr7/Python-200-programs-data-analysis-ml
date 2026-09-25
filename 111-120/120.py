# Duplicate checker

numbers = [10, 20, 30, 10, 40, 20, 50]

unique_numbers = set(numbers)

if len(numbers) == len(unique_numbers):
    print("No Duplicate")

else:
    print("Duplicates found.")
