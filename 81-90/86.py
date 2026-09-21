# Find Duplicate values

numbers = [10, 20, 30, 10, 25, 30]

duplicate_number = []

for d_number in numbers:
    if numbers.count(d_number) > 1 and d_number not in duplicate_number:
        duplicate_number.append(d_number)

print("duplicates: ", duplicate_number)