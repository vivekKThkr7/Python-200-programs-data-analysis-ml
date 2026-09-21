# Remove duplicates

numbers = [10, 20, 30, 40, 50, 50, 10]

unique_number = []

for number in numbers:
    if number not in unique_number:
        unique_number.append(number)

print(unique_number)