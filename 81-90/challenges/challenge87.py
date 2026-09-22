# Create a new list with duplicates removed:

numbers = [10, 20, 30, 40, 50, 50]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)